"""
Pydantic models for the Todo API.

This module contains all the data models used for API requests and responses,
including input validation and output serialization models.
"""
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel

# Base models
class TodoBase(BaseModel):
  """Base model for Todo items with common fields."""
  title: str
  completed: bool = False

# Input models for API requests
class TodoCreate(TodoBase):
  """Model for creating new Todo items."""

class TodoUpdate(BaseModel):
  """Model for updating existing Todo items with optional fields."""
  title: Optional[str] = None
  completed: Optional[bool] = None

# Output models for API responses
class Todo(TodoBase):
  """Complete Todo model with all fields including auto-generated ones."""
  id: int
  created_at: datetime

# API Response models
class DeleteResponse(BaseModel):
  """Response model for delete operations."""
  message: str

class TodoListResponse(BaseModel):
  """Response model for listing Todo items."""
  todos: List[Todo]
  count: int

class HealthResponse(BaseModel):
  """Response model for health check endpoint."""
  status: str

class MessageResponse(BaseModel):
  """Generic response model for simple messages."""
  message: str
