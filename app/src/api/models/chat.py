import pydantic

from .message import MessageAnnotation, SystemMessage


class Chat(pydantic.BaseModel):
    chat_id: str
    messages: list[MessageAnnotation] = pydantic.Field(default_factory=list)


class ChatResponse(pydantic.BaseModel):
    chat_id: str
    message: SystemMessage
