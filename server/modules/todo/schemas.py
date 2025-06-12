"""
Pydantic schemas for Todo API requests and responses.

This module contains Pydantic models for validating API inputs and outputs
for todo-related operations.
"""

from datetime import datetime

from pydantic import BaseModel


# Base schemas
class TodoBase(BaseModel):
  """Base model for Todo items with common fields."""

  title: str
  completed: bool = False


# Input schemas for API requests
class TodoCreate(TodoBase):
  """Schema for creating new Todo items."""


class TodoUpdate(BaseModel):
  """Schema for updating existing Todo items with optional fields."""

  title: str | None = None
  completed: bool | None = None


# Output schemas for API responses
class TodoResponse(BaseModel):
  """Complete Todo schema with all fields including auto-generated ones."""

  id: int
  title: str
  completed: bool
  created_at: datetime


class DeleteResponse(BaseModel):
  """Response schema for delete operations."""

  message: str


class TodoListResponse(BaseModel):
  """Response schema for listing Todo items."""

  todos: list[TodoResponse]
  count: int
