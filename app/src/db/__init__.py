import sqlmodel

from .models import WaitlistSubscribe

SQLITE_FILE = "sqlite:///database.db"
engine = sqlmodel.create_engine(SQLITE_FILE, echo=False)


def init_db():
    sqlmodel.SQLModel.metadata.create_all(engine)


def add_to_waitlist(email: str) -> WaitlistSubscribe:
    waitlist_subscribe = WaitlistSubscribe(email=email)
    with sqlmodel.Session(engine) as session:
        session.add(waitlist_subscribe)
        session.commit()
        session.refresh(waitlist_subscribe)
    return waitlist_subscribe
