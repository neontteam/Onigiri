import functools
import os
from typing import TypedDict

from .config import ModelVariant

APICredentials = TypedDict("APICredentials", {"api_key": str, "token": str | None, "organization": str | None})


class CredentialProvider:
    @functools.cache
    @staticmethod
    def get_credentials(model_type: ModelVariant) -> APICredentials:
        match model_type:
            case ModelVariant.GPT3_5_TURBO:
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
