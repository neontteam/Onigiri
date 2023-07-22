from datetime import datetime
from typing import Optional

import pydantic
import sqlmodel


class WaitlistSubscribe(sqlmodel.SQLModel, table=True):  # type: ignore
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    email: pydantic.EmailStr = sqlmodel.Field(nullable=False, unique=True)
    created_at: datetime = sqlmodel.Field(default_factory=datetime.utcnow)

    class Config:
        orm_mode = True
        tablename = "waitlist_subscribe"
