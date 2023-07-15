import random
import traceback
import uuid
from datetime import datetime, timezone

import pydantic
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.core.services.accounts import hash_password, verify_password
from src.api.models import (
    Chat,
    ChatResponse,
    LoginRequest,
    Message,
    MessageAnnotation,
    MessageAuthor,
    SystemMessage,
    UserMessage,
)

DEFAULT_TIMESTAMP = datetime(1970, 1, 1, tzinfo=timezone.utc)

app = FastAPI()

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_random_message(author: str | None = None) -> Message:
    _author = (
        random.choice(list(MessageAuthor)) if author is None else MessageAuthor(author)
    )
    match _author:
        case MessageAuthor.USER:
            message = "Hello, System!"
        case MessageAuthor.SYSTEM:
            message = "Hello, User!"
        case other:
            raise ValueError(f"Invalid author: {other}")
    return pydantic.parse_obj_as(
        MessageAnnotation,
        dict(
            author=_author.value,
            message=message,
            sent_timestamp=DEFAULT_TIMESTAMP.isoformat(),
        ),
    )


@app.get("/")
async def root():
    """Root of the API, returns the status 418 (GET)"""
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"msg": "I'm a teapot"}
    )


@app.get("/health-check")
async def health_check():
    """Health check (GET)"""
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"msg": "Server is healthy!"}
    )


@app.post("/login")
async def login(request: LoginRequest):
    """Login user (POST)"""
    username = "admin"
    password = hash_password("admin")
    if username == request.username and verify_password(
        password, request.password.get_secret_value()
    ):
        # I should send a redirect here, but I'm lazy
        return JSONResponse(
            status_code=status.HTTP_200_OK, content={"msg": "Login successful!"}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED, content={"msg": "Login failed!"}
        )


@app.post("/chats/new", response_model=Chat)
async def new_chat():
    """Creates a new chat (POST)"""
    try:
        chat = Chat(chat_id=uuid.uuid4().hex)
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(chat)
        )
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Could not create new chat session."},
        )


@app.get("/chats/list", response_model=list[str])
async def list_chats():
    """Lists all chats (GET)"""
    try:
        num_chats = random.randint(1, 10)
        chats: list[str] = [uuid.uuid4().hex for _ in range(num_chats)]
        return JSONResponse(status_code=status.HTTP_200_OK, content=chats)
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Could not get list of chats."},
        )


@app.get("/chats/{chat_id}/chat", response_model=Chat)
async def chat(chat_id: str):
    """Retrieves a specific chat by `chat_id` (GET)"""
    try:
        num_messages = random.randint(1, 20)
        messages: list[Message] = [get_random_message() for _ in range(num_messages)]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(Chat(chat_id=chat_id, messages=messages)),
        )
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Could not get chat messages."},
        )


@app.post("/chats/{chat_id}/chat/input", response_model=ChatResponse)
async def chat_input(chat_id: str, request: UserMessage):
    """Posts input to a specific chat identified by `chat_id` (POST)"""
    try:
        message: SystemMessage = get_random_message(author="system")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=jsonable_encoder(ChatResponse(chat_id=chat_id, message=message)),
        )
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Could not process input message."},
        )


@app.delete("/chats/{chat_id}/delete")
async def chat_delete(chat_id: str):
    """Deletes a specific chat by `chat_id` (DELETE)"""
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=dict(chat_id=chat_id, message="Done!"),
        )
    except Exception:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": "Could not process input message."},
        )
