from .config import LanguageModelConfig, LanguageModelType
from .credentials_provider import CredentialProvider
from .prompts import SystemPromptType, system_prompt_library

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage


class LanguageModelService:
    def __init__(self, model_type: LanguageModelType, model_config: LanguageModelConfig):
        self.model_type = model_type
        self.model_config = model_config
        self.credential_provider = CredentialProvider(model_type)

        match self.model_type:
            case LanguageModelType.GPT3_5_TURBO:
                credentials = self.credential_provider.get_credentials()
                self.client = ChatOpenAI(
                    openai_api_key=credentials["api_key"],
                    openai_organization=credentials["organization"],
                    model=str(self.model_type),
                    model_kwargs=self.model_config.dict(exclude_defaults=True),
                )
            case _:
                raise NotImplementedError("This model is not supported yet.")

    def process(self, user_prompt: str, system_prompt: SystemPromptType | str) -> str:
        """Process the user prompt and return the response from the model. If system_prompt is a string, it is used as the prompt.
        If it is a PromptType, the prompt is selected from the prompt library."""
        if isinstance(system_prompt, str):
            system_prompts = [SystemMessage(content=system_prompt)]
        elif isinstance(system_prompt, SystemPromptType):
            system_prompts = system_prompt_library[system_prompt]

        response: AIMessage = self.client.predict_messages(
            messages=[*system_prompts, HumanMessage(content=user_prompt)],
        )
        return response.content
