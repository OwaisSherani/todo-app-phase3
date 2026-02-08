from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import datetime


class Message(SQLModel, table=True):
    __tablename__ = "messages"

    id: int = Field(default=None, primary_key=True, nullable=False)
    conversation_id: int = Field(foreign_key="conversations.id", nullable=False)
    sender: str = Field(nullable=False)  # 'user' or 'assistant'
    content: str = Field(nullable=False)
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    # Relationship
    conversation: "Conversation" = Relationship(back_populates="messages")


# Import at the end to avoid circular imports
if TYPE_CHECKING:
    from .conversation import Conversation