import enum
import uuid
from datetime import datetime, timezone
from typing import Annotated, Literal, Union

import pydantic


def add_utc_timezone(value: datetime) -> datetime:
    return value.replace(tzinfo=timezone.utc) if value.tzinfo is None else value.astimezone(timezone.utc)


class MessageAuthor(str, enum.Enum):
    USER = "user"
    AGENT = "agent"


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


class AgentMessage(Message):
    author: Literal[MessageAuthor.AGENT] = pydantic.Field(MessageAuthor.AGENT, const=True)


MessageAnnotation = Annotated[Union[UserMessage, AgentMessage], pydantic.Field(discriminator="author")]
