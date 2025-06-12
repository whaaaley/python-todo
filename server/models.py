"""
Tortoise ORM models and Pydantic schemas for the Todo API.

This module contains Tortoise ORM models for database operations
and Pydantic models for API requests and responses.
"""

from datetime import datetime

from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model


# Tortoise ORM Models
class Todo(Model):
  id = fields.IntField(primary_key=True)
  title = fields.CharField(max_length=255)
  completed = fields.BooleanField(default=False)
  created_at = fields.DatetimeField(auto_now_add=True)

  class Meta(Model.Meta):
    table = 'todos'


# Pydantic Models for API
class TodoBase(BaseModel):
  """Base model for Todo items with common fields."""

  title: str
  completed: bool = False


# Input models for API requests
class TodoCreate(TodoBase):
  """Model for creating new Todo items."""


class TodoUpdate(BaseModel):
  """Model for updating existing Todo items with optional fields."""

  title: str | None = None
  completed: bool | None = None


# Output models for API responses
class TodoResponse(BaseModel):
  """Complete Todo model with all fields including auto-generated ones."""

  id: int
  title: str
  completed: bool
  created_at: datetime


# API Response models
class DeleteResponse(BaseModel):
  """Response model for delete operations."""

  message: str


class TodoListResponse(BaseModel):
  """Response model for listing Todo items."""

  todos: list[TodoResponse]
  count: int


class HealthResponse(BaseModel):
  """Response model for health check endpoint."""

  status: str


class MessageResponse(BaseModel):
  """Generic response model for simple messages."""

  message: str
