import json
import os
from openai import OpenAI

from .config_store import get_config
from .schemas import GeneratePromptResponse


def generate_furniture_prompt(user_request: str) -> GeneratePromptResponse:
    config = get_config()

    combined_instructions = f"""
{config["system_prompt"]}

--- MANUFACTURING RULES ---

{config["manufacturing_rules"]}
"""

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5"),
        instructions=combined_instructions,
        input=user_request,
    )

    raw = response.output_text.strip()

    # The System Prompt requires valid JSON only.
    # We still validate it before returning anything to the frontend.
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Model returned invalid JSON: {raw[:500]}"
        ) from exc

    return GeneratePromptResponse.model_validate(data)
