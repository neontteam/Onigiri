from langchain.chat_models import ChatOpenAI
from langchain.llms.base import BaseLLM

from .config import LanguageModelConfig, ModelVariant
from .credentials_provider import CredentialProvider


def get_client(config: LanguageModelConfig) -> BaseLLM:
    match config.variant:
        case ModelVariant.GPT3_5_TURBO:
            credentials = CredentialProvider.get_credentials(config.variant)
            return ChatOpenAI(
                openai_api_key=credentials["api_key"],
                openai_organization=credentials["organization"],
                model=str(config.variant),
                model_kwargs=config.dict(exclude_defaults=True),
            )
        case _:
            raise NotImplementedError("This model is not supported yet.")
