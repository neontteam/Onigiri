import enum
from typing import Literal

import pydantic

__all__ = ["LanguageModelType", "LanguageModelConfig", "GPT35TurboConfig"]


class LanguageModelType(str, enum.Enum):
    GPT3_5_TURBO = "gpt-3.5-turbo"


class LanguageModelConfig(pydantic.BaseModel):
    variant: LanguageModelType


# Open AI Models


class GPT35TurboConfig(LanguageModelConfig):
    variant: Literal[LanguageModelType.GPT3_5_TURBO] = pydantic.Field(LanguageModelType.GPT3_5_TURBO, const=True)
    max_tokens: int = 100
    temperature: float = 0.9
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    stop: list[str] = pydantic.Field(default_factory=list)
    best_of: int = 1
    n: int = 1
    stream: bool = False
    logprobs: int | None = None
    echo: bool = False
    stop_sequence: list[str] = pydantic.Field(default_factory=list)
    restart_sequence: list[str] = pydantic.Field(default_factory=list)
    return_full_text: bool = False
    return_prompt: bool = False
    expand: bool = False
    logit_bias: dict[str, float] = pydantic.Field(default_factory=dict)
