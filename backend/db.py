from sqlmodel import create_engine, Session, select
from typing import Generator
from src.config.environment import settings
from .models import Task


# Create the database engine
engine = create_engine(
    settings.database_url,
    echo=True,  # Set to True for debugging SQL queries
    pool_pre_ping=True,     # Verify connections before use
    pool_recycle=300       # Recycle connections after 5 minutes
)

def get_session() -> Generator[Session, None, None]:
    """
    Get a database session.

    This function provides a database session to be used with dependency injection.
    """
    with Session(engine) as session:
        yield session


def get_user_tasks_query(user_id: str):
    """
    Create a query to get tasks for a specific user only.

    This ensures user-level data isolation by filtering all queries by user_id.

    Args:
        user_id: The ID of the user whose tasks to retrieve

    Returns:
        A SQLModel select query for the user's tasks
    """
    return select(Task).where(Task.user_id == user_id)


def get_user_task_by_id_query(user_id: str, task_id: int):
    """
    Create a query to get a specific task for a specific user only.

    This ensures user-level data isolation by filtering by both user_id and task_id.

    Args:
        user_id: The ID of the user whose task to retrieve
        task_id: The ID of the task to retrieve

    Returns:
        A SQLModel select query for the specific user's task
    """
    return select(Task).where(Task.user_id == user_id, Task.id == task_id)