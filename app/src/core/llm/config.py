import dataclasses
import enum
from typing import Any, Literal

import pydantic
from langchain.schema import SystemMessage

from .prompts import SystemPromptType, system_prompt_library

__all__ = ["ModelVariant", "LanguageModelConfig", "GPT3_5TurboConfig", "LanguageModelServiceConfig"]


class ModelVariant(str, enum.Enum):
    GPT3_5_TURBO = "gpt-3.5-turbo"


@dataclasses.dataclass
class LanguageModelServiceConfig:
    system_prompts: list[SystemMessage] = dataclasses.field(default_factory=list)
    override_model_config: dict[str, Any] = dataclasses.field(default_factory=dict)

    @classmethod
    def basic(cls) -> "LanguageModelServiceConfig":
        return cls(system_prompts=system_prompt_library[SystemPromptType.BASIC])


class LanguageModelConfig(pydantic.BaseModel):
    variant: ModelVariant

    @classmethod
    def from_model_variant(cls, variant: ModelVariant, **config_kwargs) -> "LanguageModelConfig":
        match variant:
            case ModelVariant.GPT3_5_TURBO:
                return GPT3_5TurboConfig.parse_obj(config_kwargs)
            case _:
                raise NotImplementedError("This model is not supported yet.")


# Open AI Models
class GPT3_5TurboConfig(LanguageModelConfig):
    variant: Literal[ModelVariant.GPT3_5_TURBO] = pydantic.Field(ModelVariant.GPT3_5_TURBO, const=True)
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
