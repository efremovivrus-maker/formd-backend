import os

from dotenv import load_dotenv

load_dotenv()

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .ai import generate_furniture_prompt
from .config_store import get_config, save_config
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
    version="0.1.0",
)

origins = [
    item.strip()
    for item in os.getenv("ALLOWED_ORIGINS", "").split(",")
    if item.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT"],
    allow_headers=["Content-Type", "X-Admin-Token"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
    "/generate-prompt",
    response_model=GeneratePromptResponse,
)
def generate_prompt(payload: GeneratePromptRequest):
    try:
        # Отправляем уведомление только при первом запросе пользователя
        if not payload.clarifications:
            send_n8n_event(
                "new_request",
                request=payload.request,
            )

        # FORMD AI анализирует запрос с учетом уточнений
        result = generate_furniture_prompt(
            payload.request,
            payload.clarifications,
        )

        # Если промт уже создан — отправляем его в n8n
        if result.status != "needs_clarification" and result.prompt:
            send_n8n_event(
                "prompt_created",
                request=payload.request,
                prompt=result.prompt,
            )

        return result

    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get(
    "/admin/config",
    response_model=AdminConfigResponse,
    dependencies=[Depends(require_admin_token)],
)
def admin_get_config():
    return get_config()


@app.put(
    "/admin/config",
    response_model=AdminConfigResponse,
    dependencies=[Depends(require_admin_token)],
)
def admin_update_config(payload: AdminConfigUpdate):
    return save_config(
        system_prompt=payload.system_prompt,
        manufacturing_rules=payload.manufacturing_rules,
    )