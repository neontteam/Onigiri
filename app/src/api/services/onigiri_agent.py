from src.core.llm.client import get_client
from src.core.llm.config import (
    LanguageModelConfig,
    LanguageModelServiceConfig,
    ModelVariant,
)
from src.core.llm.service import LanguageModelService


def get_simple_llm_service(**override_client_config) -> LanguageModelService:
    service_config = LanguageModelServiceConfig.basic()
    client_config = LanguageModelConfig.from_model_variant(ModelVariant.GPT3_5_TURBO, **override_client_config)
    client = get_client(config=client_config)
    return LanguageModelService(client=client, service_config=service_config)
