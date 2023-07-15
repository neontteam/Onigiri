import enum
import uuid
from datetime import datetime, timezone
from typing import Annotated, Literal, Union

import pydantic


def add_utc_timezone(value: datetime) -> datetime:
    return value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value.astimezone(timezone.utc)


class LoginRequest(pydantic.BaseModel):
    username: str
    password: pydantic.SecretStr


class MessageAuthor(str, enum.Enum):
    USER = "user"
    SYSTEM = "system"


class Message(pydantic.BaseModel):
    id: str = pydantic.Field(default_factory=lambda: uuid.uuid4().hex, const=True)
    receive_timestamp: datetime = pydantic.Field(default_factory=datetime.utcnow, const=True)
    sent_timestamp: datetime
    author: MessageAuthor
    message: str

    _add_utc_timezone = pydantic.validator(
        "sent_timestamp",
        allow_reuse=True,
    )(add_utc_timezone)

    _add_utc_timezone = pydantic.validator(
        "receive_timestamp",
        allow_reuse=True,
    )(add_utc_timezone)


class UserMessage(Message):
    author: Literal[MessageAuthor.USER] = pydantic.Field(MessageAuthor.USER, const=True)


class SystemMessage(Message):
    author: Literal[MessageAuthor.SYSTEM] = pydantic.Field(MessageAuthor.SYSTEM, const=True)


MessageAnnotation = Annotated[Union[UserMessage, SystemMessage], pydantic.Field(discriminator="author")]


class Chat(pydantic.BaseModel):
    chat_id: str
    messages: list[MessageAnnotation] = pydantic.Field(default_factory=list)


class ChatResponse(pydantic.BaseModel):
    chat_id: str
    message: SystemMessage
