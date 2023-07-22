import pydantic


class LoginRequest(pydantic.BaseModel):
    username: str
    password: pydantic.SecretStr


class SubscribeWaitlistRequest(pydantic.BaseModel):
    email: pydantic.EmailStr
