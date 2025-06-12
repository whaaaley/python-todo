"""
Tortoise ORM models for the Todo API.

This module contains Tortoise ORM models for database operations.
Pydantic schemas are now located in their respective module schemas files.
"""

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


# General API Response models (shared across modules)
class HealthResponse(BaseModel):
  """Response model for health check endpoint."""

  status: str


class MessageResponse(BaseModel):
  """Generic response model for simple messages."""

  message: str
