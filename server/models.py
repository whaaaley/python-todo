from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

# Base models
class TodoBase(BaseModel):
    """Base model with common todo fields"""
    title: str
    completed: bool = False

# Input models for API requests
class TodoCreate(TodoBase):
    """Model for creating a new todo"""
    pass

class TodoUpdate(BaseModel):
    """Model for updating an existing todo (all fields optional)"""
    title: Optional[str] = None
    completed: Optional[bool] = None

# Output models for API responses
class Todo(TodoBase):
    """Complete todo model with all fields"""
    id: int
    created_at: datetime

# API Response models
class DeleteResponse(BaseModel):
    """Response model for delete operations"""
    message: str

class TodoListResponse(BaseModel):
    """Response model for paginated todo lists"""
    todos: List[Todo]
    count: int

class HealthResponse(BaseModel):
    """Response model for health check"""
    status: str

class MessageResponse(BaseModel):
    """Generic message response"""
    message: str
