from typing import Literal, Optional
from pydantic import BaseModel, Field


class GeneratePromptRequest(BaseModel):
    request: str = Field(min_length=3, max_length=5000)


class GeneratePromptResponse(BaseModel):
    status: Literal["ok", "adapted", "insufficient_data"]
    object_type: str
    concept: str
    adaptations: list[str]
    prompt: str
    manufacturing_note: str


class AdminConfigResponse(BaseModel):
    version: int
    updated_at: Optional[str]
    system_prompt: str
    manufacturing_rules: str


class AdminConfigUpdate(BaseModel):
    system_prompt: str = Field(min_length=100)
    manufacturing_rules: str = Field(min_length=100)
