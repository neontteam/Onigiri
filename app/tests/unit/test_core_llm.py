import pytest

from src.core.llm import GPT35TurboConfig, LanguageModelService, LanguageModelType


def test_llm_service_init():
    service = LanguageModelService(model_type=LanguageModelType.GPT3_5_TURBO, model_config=GPT35TurboConfig())
    assert service is not None
