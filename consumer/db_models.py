import uuid

from consumer.database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    text = Column(String(length=1000), nullable=False, index=True)
