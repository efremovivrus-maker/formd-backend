import json
import os

from openai import OpenAI

from .config_store import get_config
from .schemas import ClarificationItem, GeneratePromptResponse


def generate_furniture_prompt(
    user_request: str,
    clarifications: list[ClarificationItem],
) -> GeneratePromptResponse:

    config = get_config()

    combined_instructions = f"""
{config["system_prompt"]}

--- MANUFACTURING RULES ---

{config["manufacturing_rules"]}
"""

    # Собираем исходный запрос + предыдущие уточнения
    input_parts = [
        f"ORIGINAL USER REQUEST:\n{user_request}"
    ]

    if clarifications:
        input_parts.append("\nCLARIFICATIONS PROVIDED BY USER:")

        for index, item in enumerate(clarifications, start=1):
            input_parts.append(
                f"\n{index}. Question: {item.question}\n"
                f"Answer: {item.answer}"
            )

    model_input = "\n".join(input_parts)

    client = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"]
    )

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        instructions=combined_instructions,
        input=model_input,
    )

    raw = response.output_text.strip()

    # System Prompt требует только валидный JSON.
    # Дополнительно проверяем результат перед отправкой frontend.
    try:
        data = json.loads(raw)

    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Model returned invalid JSON: {raw[:500]}"
        ) from exc

    return GeneratePromptResponse.model_validate(data)