import uuid
from sqlalchemy.dialects.postgresql.base import UUID

from sqlalchemy.exc import DatabaseError

from consumer.database import get_db_session
from consumer.db_models import Message


def create_message(new_message: str) -> Message:
    if not new_message:
        return
    session = get_db_session()
    message = Message(text=new_message)
    session.add(message)
    session.commit()
    return message


def get_messages_count() -> int:
    session = get_db_session()
    return session.query(Message.id).count()


def get_message_by_id(id: UUID) -> Message:
    try:
        session = get_db_session()
        return session.query(Message).get(id)
    except DatabaseError:
        print("Invalid id")
