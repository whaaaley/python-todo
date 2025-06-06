from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

# Base models
class TodoBase(BaseModel):
  title: str
  completed: bool = False

# Input models for API requests
class TodoCreate(TodoBase):
  pass

class TodoUpdate(BaseModel):
  title: Optional[str] = None
  completed: Optional[bool] = None

# Output models for API responses
class Todo(TodoBase):
  id: int
  created_at: datetime

# API Response models
class DeleteResponse(BaseModel):
  message: str

class TodoListResponse(BaseModel):
  todos: List[Todo]
  count: int

class HealthResponse(BaseModel):
  status: str

class MessageResponse(BaseModel):
  message: str
