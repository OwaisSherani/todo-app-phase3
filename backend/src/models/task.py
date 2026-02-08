from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    completed = "completed"


class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: str = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: int = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(nullable=False, max_length=255)
    description: Optional[str] = Field(default=None)
    status: TaskStatus = Field(default=TaskStatus.pending)
    user_id: str = Field(foreign_key="users.id", nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    # Relationship
    user: User = Relationship(back_populates="tasks")


class Conversation(SQLModel, table=True):
    __tablename__ = "conversations"
    
    id: int = Field(default=None, primary_key=True, nullable=False)
    user_id: str = Field(foreign_key="users.id", nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    # Relationships
    user: User = Relationship(back_populates="conversations")
    messages: list["Message"] = Relationship(back_populates="conversation")


class Message(SQLModel, table=True):
    __tablename__ = "messages"
    
    id: int = Field(default=None, primary_key=True, nullable=False)
    conversation_id: int = Field(foreign_key="conversations.id", nullable=False)
    sender: str = Field(nullable=False)  # 'user' or 'assistant'
    content: str = Field(nullable=False)
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    
    # Relationship
    conversation: Conversation = Relationship(back_populates="messages")