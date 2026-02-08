"""
MCP Server implementation for task management
"""
import asyncio
from typing import Dict, Any, List
from uuid import UUID
from mcp.server import Server
from mcp.types import TextContent, Resource, Tool
from pydantic import BaseModel, Field
from sqlmodel import select
from database import engine
from models import Task


class CreateTaskRequest(BaseModel):
    title: str = Field(..., description="Title of the task")
    description: str = Field("", description="Description of the task")


class GetTaskRequest(BaseModel):
    task_id: UUID = Field(..., description="ID of the task to retrieve")


class UpdateTaskRequest(BaseModel):
    task_id: UUID = Field(..., description="ID of the task to update")
    title: str = Field(None, description="New title of the task")
    description: str = Field(None, description="New description of the task")
    completed: bool = Field(None, description="Whether the task is completed")


class DeleteTaskRequest(BaseModel):
    task_id: UUID = Field(..., description="ID of the task to delete")


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str


class TasksResponse(BaseModel):
    tasks: List[TaskResponse]


class TaskMCPService:
    def __init__(self):
        self.server = Server("task-manager-mcp")
        
    async def initialize(self):
        """Initialize the MCP server with tools"""
        # Define tools
        await self.server.set_tools([
            Tool(
                name="create_task",
                description="Create a new task for the authenticated user",
                input_schema={
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Title of the task"},
                        "description": {"type": "string", "description": "Description of the task"}
                    },
                    "required": ["title"]
                }
            ),
            Tool(
                name="get_tasks",
                description="Get all tasks for the authenticated user",
                input_schema={
                    "type": "object",
                    "properties": {}
                }
            ),
            Tool(
                name="get_task",
                description="Get a specific task by ID for the authenticated user",
                input_schema={
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "format": "uuid", "description": "ID of the task to retrieve"}
                    },
                    "required": ["task_id"]
                }
            ),
            Tool(
                name="update_task",
                description="Update a specific task by ID for the authenticated user",
                input_schema={
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "format": "uuid", "description": "ID of the task to update"},
                        "title": {"type": "string", "description": "New title of the task"},
                        "description": {"type": "string", "description": "New description of the task"},
                        "completed": {"type": "boolean", "description": "Whether the task is completed"}
                    },
                    "required": ["task_id"]
                }
            ),
            Tool(
                name="delete_task",
                description="Delete a specific task by ID for the authenticated user",
                input_schema={
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "format": "uuid", "description": "ID of the task to delete"}
                    },
                    "required": ["task_id"]
                }
            )
        ])
        
        # Register handlers
        self.server.create_tool_handler("create_task")(self.handle_create_task)
        self.server.create_tool_handler("get_tasks")(self.handle_get_tasks)
        self.server.create_tool_handler("get_task")(self.handle_get_task)
        self.server.create_tool_handler("update_task")(self.handle_update_task)
        self.server.create_tool_handler("delete_task")(self.handle_delete_task)
    
    async def handle_create_task(self, *, title: str, description: str = "", **kwargs) -> List[Dict[str, Any]]:
        """
        Create a new task for the authenticated user
        """
        try:
            # Extract user_id from context (this would come from JWT in a real implementation)
            user_id = kwargs.get('user_id', 'default_user')
            
            with Session(engine) as session:
                task = Task(
                    title=title,
                    description=description,
                    completed=False,
                    user_id=user_id
                )
                session.add(task)
                session.commit()
                session.refresh(task)
                
                return [{
                    "result": {
                        "id": str(task.id),
                        "title": task.title,
                        "description": task.description,
                        "completed": task.completed,
                        "created_at": task.created_at.isoformat(),
                        "updated_at": task.updated_at.isoformat()
                    }
                }]
        except Exception as e:
            return [{"error": f"Failed to create task: {str(e)}"}]
    
    async def handle_get_tasks(self, **kwargs) -> List[Dict[str, Any]]:
        """
        Get all tasks for the authenticated user
        """
        try:
            # Extract user_id from context (this would come from JWT in a real implementation)
            user_id = kwargs.get('user_id', 'default_user')
            
            with Session(engine) as session:
                statement = select(Task).where(Task.user_id == user_id)
                tasks = session.exec(statement).all()
                
                return [{
                    "result": {
                        "tasks": [
                            {
                                "id": str(task.id),
                                "title": task.title,
                                "description": task.description,
                                "completed": task.completed,
                                "created_at": task.created_at.isoformat(),
                                "updated_at": task.updated_at.isoformat()
                            }
                            for task in tasks
                        ]
                    }
                }]
        except Exception as e:
            return [{"error": f"Failed to get tasks: {str(e)}"}]
    
    async def handle_get_task(self, *, task_id: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Get a specific task by ID for the authenticated user
        """
        try:
            # Extract user_id from context (this would come from JWT in a real implementation)
            user_id = kwargs.get('user_id', 'default_user')
            
            with Session(engine) as session:
                task = session.get(Task, UUID(task_id))
                
                if not task:
                    return [{"error": "Task not found"}]
                
                if task.user_id != user_id:
                    return [{"error": "Access denied: Task does not belong to user"}]
                
                return [{
                    "result": {
                        "id": str(task.id),
                        "title": task.title,
                        "description": task.description,
                        "completed": task.completed,
                        "created_at": task.created_at.isoformat(),
                        "updated_at": task.updated_at.isoformat()
                    }
                }]
        except Exception as e:
            return [{"error": f"Failed to get task: {str(e)}"}]
    
    async def handle_update_task(self, *, task_id: str, title: str = None, 
                                 description: str = None, completed: bool = None, **kwargs) -> List[Dict[str, Any]]:
        """
        Update a specific task by ID for the authenticated user
        """
        try:
            # Extract user_id from context (this would come from JWT in a real implementation)
            user_id = kwargs.get('user_id', 'default_user')
            
            with Session(engine) as session:
                task = session.get(Task, UUID(task_id))
                
                if not task:
                    return [{"error": "Task not found"}]
                
                if task.user_id != user_id:
                    return [{"error": "Access denied: Task does not belong to user"}]
                
                # Update fields if provided
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if completed is not None:
                    task.completed = completed
                
                session.add(task)
                session.commit()
                session.refresh(task)
                
                return [{
                    "result": {
                        "id": str(task.id),
                        "title": task.title,
                        "description": task.description,
                        "completed": task.completed,
                        "created_at": task.created_at.isoformat(),
                        "updated_at": task.updated_at.isoformat()
                    }
                }]
        except Exception as e:
            return [{"error": f"Failed to update task: {str(e)}"}]
    
    async def handle_delete_task(self, *, task_id: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Delete a specific task by ID for the authenticated user
        """
        try:
            # Extract user_id from context (this would come from JWT in a real implementation)
            user_id = kwargs.get('user_id', 'default_user')
            
            with Session(engine) as session:
                task = session.get(Task, UUID(task_id))
                
                if not task:
                    return [{"error": "Task not found"}]
                
                if task.user_id != user_id:
                    return [{"error": "Access denied: Task does not belong to user"}]
                
                session.delete(task)
                session.commit()
                
                return [{"result": {"success": True}}]
        except Exception as e:
            return [{"error": f"Failed to delete task: {str(e)}"}]
    
    async def run(self):
        """Run the MCP server"""
        await self.initialize()
        return self.server


# Global instance
mcp_service = TaskMCPService()