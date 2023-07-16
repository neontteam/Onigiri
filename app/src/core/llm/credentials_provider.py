import functools
import os
from typing import TypedDict

from .config import LanguageModelType

APICredentials = TypedDict("APICredentials", {"api_key": str, "token": str | None, "organization": str | None})


class CredentialProvider:
    def __init__(self, model_type: LanguageModelType):
        self.model_type = model_type

    @functools.cache
    def get_credentials(self) -> APICredentials:
        match self.model_type:
            case LanguageModelType.GPT3_5_TURBO:
                try:
                    return {
                        "api_key": os.environ["OPENAI_API_KEY"],
                        "token": None,
                        "organization": os.environ.get("OPENAI_ORGANIZATION"),
                    }
                except KeyError:
                    raise RuntimeError("OPENAI_API_KEY environment variable is not set.")
            case _:
                raise NotImplementedError("This model is not supported yet.")
