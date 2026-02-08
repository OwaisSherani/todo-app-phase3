"""
Task router with JWT authentication
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from typing import List
from uuid import UUID
from backend.models import Task, TaskCreate, TaskUpdate
from backend.auth import get_current_user_from_token
from backend.schemas import TaskResponse
from backend.db import get_session


router = APIRouter()


@router.post("/tasks/", response_model=TaskResponse)
async def create_task_api(task_data: TaskCreate, user_id: str = Depends(get_current_user_from_token), session=Depends(get_session)):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        user_id=user_id
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return TaskResponse.from_orm(task)


@router.get("/tasks/", response_model=List[TaskResponse])
async def get_tasks_api(user_id: str = Depends(get_current_user_from_token), session=Depends(get_session)):
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return [TaskResponse.from_orm(task) for task in tasks]


@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task_api(task_id: UUID, user_id: str = Depends(get_current_user_from_token), session=Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")
    return TaskResponse.from_orm(task)


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task_api(task_id: UUID, task_data: TaskUpdate, user_id: str = Depends(get_current_user_from_token), session=Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    # Update fields
    if task_data.title is not None:
        task.title = task_data.title
    if task_data.description is not None:
        task.description = task_data.description
    if task_data.completed is not None:
        task.completed = task_data.completed

    session.add(task)
    session.commit()
    session.refresh(task)
    return TaskResponse.from_orm(task)


@router.delete("/tasks/{task_id}")
async def delete_task_api(task_id: UUID, user_id: str = Depends(get_current_user_from_token), session=Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied")

    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}