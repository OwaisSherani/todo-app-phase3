from typing import List, Optional
from sqlmodel import Session, select
from ..models.task_model import Task, TaskStatus
from ..models.user import User
from datetime import datetime


class TaskService:
    @staticmethod
    def create_task(session: Session, user_id: str, title: str, description: Optional[str] = None) -> Task:
        """
        Create a new task for a user
        """
        task = Task(
            title=title,
            description=description,
            user_id=user_id,
            status=TaskStatus.pending
        )
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @staticmethod
    def get_user_tasks(session: Session, user_id: str, status: Optional[TaskStatus] = None) -> List[Task]:
        """
        Get all tasks for a user, optionally filtered by status
        """
        query = select(Task).where(Task.user_id == user_id)
        
        if status:
            query = query.where(Task.status == status)
            
        tasks = session.exec(query).all()
        return tasks

    @staticmethod
    def get_task_by_id(session: Session, task_id: int, user_id: str) -> Optional[Task]:
        """
        Get a specific task by ID for a user
        """
        query = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(query).first()
        return task

    @staticmethod
    def update_task(
        session: Session,
        task_id: int,
        user_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[TaskStatus] = None
    ) -> Optional[Task]:
        """
        Update a task for a user
        """
        task = TaskService.get_task_by_id(session, task_id, user_id)
        if not task:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if status is not None:
            task.status = status
            
        task.updated_at = datetime.utcnow()
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

    @staticmethod
    def delete_task(session: Session, task_id: int, user_id: str) -> bool:
        """
        Delete a task for a user
        """
        task = TaskService.get_task_by_id(session, task_id, user_id)
        if not task:
            return False

        session.delete(task)
        session.commit()
        return True

    @staticmethod
    def complete_task(session: Session, task_id: int, user_id: str) -> Optional[Task]:
        """
        Mark a task as completed for a user
        """
        return TaskService.update_task(
            session=session,
            task_id=task_id,
            user_id=user_id,
            status=TaskStatus.completed
        )