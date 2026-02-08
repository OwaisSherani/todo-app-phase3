from typing import Dict, Any, Optional
from ..services.task_service import TaskService
from ..models.task_model import TaskStatus
from sqlmodel import Session
from ..database import engine


class TaskDomainAgent:
    """
    Handles task-specific operations and enforces business rules related to tasks.
    Validates inputs, handles business logic, and interacts with the TaskService.
    """

    def __init__(self):
        # Session will be created when needed
        self.session = None

    def create_task(self, user_id: str, title: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new task with validation and business rules enforcement.
        """
        # Validate inputs
        if not title or len(title.strip()) == 0:
            return {
                "success": False,
                "message": "Task title is required and cannot be empty"
            }

        if len(title) > 255:
            return {
                "success": False,
                "message": "Task title exceeds maximum length of 255 characters"
            }

        with Session(engine) as session:
            try:
                # Create the task using TaskService
                task = TaskService.create_task(
                    session=session,
                    user_id=user_id,
                    title=title,
                    description=description
                )

                return {
                    "success": True,
                    "task_id": task.id,
                    "message": f"Task '{task.title}' created successfully"
                }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Failed to create task: {str(e)}"
                }

    def get_tasks(self, user_id: str, status: Optional[str] = None) -> Dict[str, Any]:
        """
        Get tasks for a user with optional status filtering.
        """
        with Session(engine) as session:
            try:
                # Convert status string to enum if provided
                status_enum = None
                if status:
                    try:
                        status_enum = TaskStatus(status)
                    except ValueError:
                        return {
                            "success": False,
                            "tasks": [],
                            "message": f"Invalid status: {status}. Valid values are: 'pending', 'completed'"
                        }

                # Get tasks using TaskService
                tasks = TaskService.get_user_tasks(
                    session=session,
                    user_id=user_id,
                    status=status_enum
                )

                # Format tasks for response
                task_list = []
                for task in tasks:
                    task_list.append({
                        "id": task.id,
                        "title": task.title,
                        "description": task.description or "",
                        "status": task.status.value
                    })

                return {
                    "success": True,
                    "tasks": task_list,
                    "message": f"Retrieved {len(task_list)} tasks"
                }
            except Exception as e:
                return {
                    "success": False,
                    "tasks": [],
                    "message": f"Failed to retrieve tasks: {str(e)}"
                }

    def update_task(
        self,
        user_id: str,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update a task with validation and business rules enforcement.
        """
        with Session(engine) as session:
            try:
                # Validate status if provided
                status_enum = None
                if status:
                    try:
                        status_enum = TaskStatus(status)
                    except ValueError:
                        return {
                            "success": False,
                            "message": f"Invalid status: {status}. Valid values are: 'pending', 'completed'"
                        }

                # Update the task using TaskService
                updated_task = TaskService.update_task(
                    session=session,
                    task_id=task_id,
                    user_id=user_id,
                    title=title,
                    description=description,
                    status=status_enum
                )

                if updated_task:
                    return {
                        "success": True,
                        "message": f"Task {task_id} updated successfully"
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Task {task_id} not found or not owned by user"
                    }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Failed to update task: {str(e)}"
                }

    def complete_task(self, user_id: str, task_id: int) -> Dict[str, Any]:
        """
        Mark a task as completed.
        """
        with Session(engine) as session:
            try:
                # Update the task status to completed
                updated_task = TaskService.update_task(
                    session=session,
                    task_id=task_id,
                    user_id=user_id,
                    status=TaskStatus.completed
                )

                if updated_task:
                    return {
                        "success": True,
                        "message": f"Task {task_id} marked as completed"
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Task {task_id} not found or not owned by user"
                    }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Failed to complete task: {str(e)}"
                }

    def delete_task(self, user_id: str, task_id: int) -> Dict[str, Any]:
        """
        Delete a task after validating ownership.
        """
        with Session(engine) as session:
            try:
                # Delete the task using TaskService
                success = TaskService.delete_task(
                    session=session,
                    task_id=task_id,
                    user_id=user_id
                )

                if success:
                    return {
                        "success": True,
                        "message": f"Task {task_id} deleted successfully"
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Task {task_id} not found or not owned by user"
                    }
            except Exception as e:
                return {
                    "success": False,
                    "message": f"Failed to delete task: {str(e)}"
                }

    def close_session(self):
        """
        Close the database session.
        """
        # Session is handled with context manager, so no explicit closing needed
        pass