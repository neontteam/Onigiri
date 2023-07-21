import pytest
from langchain.schema import HumanMessage
from pytest_mock import MockerFixture

from src.core.llm import (
    LanguageModelService,
    LanguageModelServiceConfig,
    SystemPromptType,
    system_prompt_library,
)


def test_language_model_service_init(mocker: MockerFixture):
    mock_llm = mocker.MagicMock()
    service = LanguageModelService(client=mock_llm, service_config=LanguageModelServiceConfig.basic())
    service.process(user_prompt="hello")
    mock_llm.predict_messages.assert_called_once()
    mock_llm.predict_messages.assert_called_with(
        messages=[*system_prompt_library[SystemPromptType.BASIC], HumanMessage(content="hello")]
    )
