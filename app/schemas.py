from typing import Literal, Optional

from pydantic import BaseModel, Field


class ClarificationItem(BaseModel):
    question: str
    answer: str


class RequestCheckResponse(BaseModel):
    decision: Literal[
        "ready",
        "clarify",
        "invalid",
    ]

    question: Optional[str] = None


class GeneratePromptRequest(BaseModel):
    request: str = Field(
        min_length=3,
        max_length=5000,
    )

    clarifications: list[ClarificationItem] = Field(
        default_factory=list
    )


class GeneratePromptResponse(BaseModel):
    status: Literal[
        "ok",
        "adapted",
        "insufficient_data",
        "needs_clarification",
        "invalid_request",
    ]

    # Используется, если AI хочет задать пользователю уточняющий вопрос
    question: Optional[str] = None

    # Используются, когда AI уже может сформировать результат
    object_type: Optional[str] = None
    concept: Optional[str] = None

    adaptations: list[str] = Field(
        default_factory=list
    )

    prompt: Optional[str] = None
    manufacturing_note: Optional[str] = None


class AdminConfigResponse(BaseModel):
    version: int
    updated_at: Optional[str]
    system_prompt: str
    manufacturing_rules: str


class AdminConfigUpdate(BaseModel):
    system_prompt: str = Field(
        min_length=100
    )

    manufacturing_rules: str = Field(
        min_length=100
    )