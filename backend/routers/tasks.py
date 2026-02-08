from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session, select
from auth import get_current_user_id
from dependencies import get_db_session
from models import Task, TaskCreate, TaskUpdate, TaskRead
from uuid import UUID

router = APIRouter()


@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(
    user_id: str,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Get all tasks for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        current_user_id: The user ID extracted from the JWT token
        session: Database session for querying
        
    Returns:
        List of tasks belonging to the user
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Query for tasks belonging to the authenticated user
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    
    return tasks


@router.post("/tasks", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    user_id: str,
    task_create: TaskCreate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Create a new task for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        task_create: Task creation data
        current_user_id: The user ID extracted from the JWT token
        session: Database session for creating the task
        
    Returns:
        The created task
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Create a new task instance
    task_data = task_create.model_dump()
    task = Task(**task_data, user_id=user_id)
    
    # Add the task to the session and commit
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(
    user_id: str,
    task_id: UUID,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Get a specific task by ID for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        task_id: The ID of the task to retrieve
        current_user_id: The user ID extracted from the JWT token
        session: Database session for querying
        
    Returns:
        The requested task
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Query for the specific task belonging to the authenticated user
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return task


@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    user_id: str,
    task_id: UUID,
    task_update: TaskUpdate,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Update a specific task by ID for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        task_id: The ID of the task to update
        task_update: Task update data
        current_user_id: The user ID extracted from the JWT token
        session: Database session for updating
        
    Returns:
        The updated task
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Query for the specific task belonging to the authenticated user
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Update the task with the provided data
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    user_id: str,
    task_id: UUID,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Delete a specific task by ID for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        task_id: The ID of the task to delete
        current_user_id: The user ID extracted from the JWT token
        session: Database session for deleting
        
    Returns:
        204 No Content on successful deletion
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Query for the specific task belonging to the authenticated user
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Delete the task
    session.delete(task)
    session.commit()


@router.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion(
    user_id: str,
    task_id: UUID,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_db_session)
):
    """
    Toggle the completion status of a specific task for the authenticated user.
    
    Args:
        user_id: The user ID from the URL path
        task_id: The ID of the task to toggle
        current_user_id: The user ID extracted from the JWT token
        session: Database session for updating
        
    Returns:
        The updated task with toggled completion status
    """
    # Verify that the user_id in the URL matches the user_id in the JWT token
    if user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: user_id mismatch"
        )
    
    # Query for the specific task belonging to the authenticated user
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    task = session.exec(statement).first()
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    # Toggle the completion status
    task.completed = not task.completed
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task