from langchain.schema import AIMessage, HumanMessage

from .client import BaseLLM
from .config import LanguageModelServiceConfig


class LanguageModelService:
    def __init__(self, client: BaseLLM, service_config: LanguageModelServiceConfig):
        self._client = client
        self._config = service_config

    def process(self, user_prompt: str) -> str:
        response: AIMessage = self._client.predict_messages(
            messages=[*self._config.system_prompts, HumanMessage(content=user_prompt)],
        )
        return response.content
