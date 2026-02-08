from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime

from ..models import Task, TaskCreate, TaskUpdate
from ..db import get_session, get_user_tasks_query, get_user_task_by_id_query
from ..auth import get_current_user, verify_user_owns_resource
from ..schemas import TaskResponse, TaskCreateRequest, TaskUpdateRequest, TaskListResponse
from ..config.settings import settings


# Create the tasks router
router = APIRouter(prefix="/{user_id}/tasks", tags=["tasks"])


@router.get("/", response_model=TaskListResponse)
def get_tasks(
    user_id: str,
    current_user_id: str = Depends(get_current_user),
    completed: Optional[bool] = Query(None, description="Filter tasks by completion status"),
    session: Session = Depends(get_session)
):
    """
    Retrieve all tasks for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access these tasks"
        )

    # Build the query
    query = get_user_tasks_query(user_id)

    # Apply completion status filter if provided
    if completed is not None:
        query = query.where(Task.completed == completed)

    # Execute the query
    tasks = session.exec(query).all()

    # Convert to response model
    task_responses = [TaskResponse.model_validate(task) for task in tasks]

    return TaskListResponse(tasks=task_responses)


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task_create: TaskCreateRequest,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to create tasks for this user"
        )

    # Create the task object
    db_task = Task.model_validate(task_create, update={"user_id": user_id, "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()})

    # Add to session and commit
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return TaskResponse.model_validate(db_task)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    user_id: str,
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Retrieve a specific task for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this task"
        )

    # Get the task
    query = get_user_task_by_id_query(user_id, task_id)
    db_task = session.exec(query).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return TaskResponse.model_validate(db_task)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    user_id: str,
    task_id: int,
    task_update: TaskUpdateRequest,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Update a specific task for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    # Get the task
    query = get_user_task_by_id_query(user_id, task_id)
    db_task = session.exec(query).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Update the task with provided values
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    # Update the timestamp
    db_task.updated_at = datetime.utcnow()

    # Commit changes
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return TaskResponse.model_validate(db_task)


@router.patch("/{task_id}/complete", response_model=TaskResponse)
def toggle_task_completion(
    user_id: str,
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a specific task for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to update this task"
        )

    # Get the task
    query = get_user_task_by_id_query(user_id, task_id)
    db_task = session.exec(query).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Toggle the completion status
    db_task.completed = not db_task.completed
    db_task.updated_at = datetime.utcnow()

    # Commit changes
    session.add(db_task)
    session.commit()
    session.refresh(db_task)

    return TaskResponse.model_validate(db_task)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: str,
    task_id: int,
    current_user_id: str = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete a specific task for the authenticated user.
    """
    # Verify that the authenticated user matches the requested user_id
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )

    # Get the task
    query = get_user_task_by_id_query(user_id, task_id)
    db_task = session.exec(query).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Delete the task
    session.delete(db_task)
    session.commit()

    return