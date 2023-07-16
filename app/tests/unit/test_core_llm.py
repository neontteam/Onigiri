import pytest

from src.core.llm import LanguageModelService, LanguageModelType, GPT35TurboConfig


def test_llm_service_init():
    service = LanguageModelService(model_type=LanguageModelType.GPT3_5_TURBO, model_config=GPT35TurboConfig())
    assert service is not None
