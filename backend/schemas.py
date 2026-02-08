from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskRead(BaseModel):
    id: int
    user_id: str
    title: str
    description: Optional[str] = None
    completed: bool
    created_at: datetime
    updated_at: datetime


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None