from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    completed = "completed"


class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: int = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(nullable=False, max_length=255)
    description: Optional[str] = Field(default=None)
    status: TaskStatus = Field(default=TaskStatus.pending)
    user_id: str = Field(foreign_key="users.id", nullable=False)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)