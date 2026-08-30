import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .ai import (
    check_request,
    generate_furniture_prompt,
)
from .config_store import (
    get_config,
    save_config,
)
from .notifications import send_n8n_event
from .schemas import (
    AdminConfigResponse,
    AdminConfigUpdate,
    GeneratePromptRequest,
    GeneratePromptResponse,
)
from .security import require_admin_token


app = FastAPI(
    title="FORMD AI API",
    version="0.2.0",
)


origins = [
    item.strip()
    for item in os.getenv(
        "ALLOWED_ORIGINS",
        "",
    ).split(",")
    if item.strip()
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
    ],
    allow_headers=[
        "Content-Type",
        "X-Admin-Token",
    ],
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post(
    "/generate-prompt",
    response_model=GeneratePromptResponse,
)
def generate_prompt(
    payload: GeneratePromptRequest,
):
    try:

        # Уведомляем о новом запросе
        # только при первом сообщении пользователя
        if not payload.clarifications:
            send_n8n_event(
                "new_request",
                request=payload.request,
            )

        # -------------------------
        # FAST PRE-CHECK
        # -------------------------

        # После двух уточнений больше ничего не спрашиваем.
        # Сразу считаем данных достаточно для генерации.
        if len(payload.clarifications) >= 2:
            check = None
        else:
            check = check_request(
                payload.request,
                payload.clarifications,
            )

        # Запрос не относится к FORMD
        if check and check.decision == "invalid":

            return GeneratePromptResponse(
                status="invalid_request",
                question=None,
                object_type=None,
                concept=None,
                adaptations=[],
                prompt=None,
                manufacturing_note=(
                    "Не удалось распознать задачу "
                    "по проектированию мебели. "
                    "Опишите, какой предмет "
                    "вы хотите создать."
                ),
            )

        # Нужен уточняющий вопрос
        if check and check.decision == "clarify":

            return GeneratePromptResponse(
                status="needs_clarification",
                question=check.question,
                object_type=None,
                concept=None,
                adaptations=[],
                prompt=None,
                manufacturing_note=None,
            )

        # -------------------------
        # FULL FORMD GENERATION
        # -------------------------

        result = generate_furniture_prompt(
            payload.request,
            payload.clarifications,
        )

        # На этом этапе дополнительных
        # уточнений быть уже не должно
        if result.status == "needs_clarification":

            return GeneratePromptResponse(
                status="insufficient_data",
                question=None,
                object_type=result.object_type,
                concept=result.concept,
                adaptations=result.adaptations,
                prompt=result.prompt,
                manufacturing_note=(
                    result.manufacturing_note
                    or "Недостаточно данных для уверенной генерации."
                ),
            )

        # Отправляем готовый промт в n8n
        if result.prompt:
            send_n8n_event(
                "prompt_created",
                request=payload.request,
                prompt=result.prompt,
            )

        return result

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc


@app.get(
    "/admin/config",
    response_model=AdminConfigResponse,
    dependencies=[
        Depends(require_admin_token)
    ],
)
def admin_get_config():
    return get_config()


@app.put(
    "/admin/config",
    response_model=AdminConfigResponse,
    dependencies=[
        Depends(require_admin_token)
    ],
)
def admin_update_config(
    payload: AdminConfigUpdate,
):
    return save_config(
        system_prompt=payload.system_prompt,
        manufacturing_rules=(
            payload.manufacturing_rules
        ),
    )