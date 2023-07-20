import pydantic


class LoginRequest(pydantic.BaseModel):
    username: str
    password: pydantic.SecretStr
