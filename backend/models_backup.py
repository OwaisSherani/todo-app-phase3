"""
Database models for the task management system
"""
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, Session, create_engine, select
from uuid import UUID, uuid4
from pydantic import BaseModel


class Task(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str = Field(max_length=255)
    description: str = Field(default="")
    completed: bool = Field(default=False)
    user_id: str = Field(max_length=255)  # In a real app, this would be a foreign key to a User table

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# Database setup - This is kept for testing purposes only
# The actual engine is created in database.py using the configuration
from sqlalchemy.pool import StaticPool

def create_db_and_tables():
    # This function is kept for testing purposes
    # The actual table creation happens in main.py startup event
    pass