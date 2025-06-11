"""
Test suite for the Todo API.

This module contains integration tests for all Todo API endpoints including
create, read, update, and delete operations using FastAPI TestClient.
"""
from fastapi.testclient import TestClient
from polyfactory.factories.pydantic_factory import ModelFactory
from models import TodoCreate, TodoUpdate
from main import app

client = TestClient(app)

class TestState:
  """Container for test state."""
  todo_id = 0

test_state = TestState()

class TodoCreateFactory(ModelFactory[TodoCreate]):
  """Factory for generating TodoCreate test instances."""
  __use_examples__ = True

def test_create_todo():
  """Test creating a new todo item."""
  fake_todo_create = TodoCreateFactory.build()
  response = client.post(url='/todo/create', json=fake_todo_create.model_dump())
  test_state.todo_id = response.json()['id']
  assert response.status_code == 200

def test_update_todo():
  """Test updating an existing todo item."""
  update_data = TodoUpdate(title='Updated Title')
  response = client.put(url=f'/todo/update/{test_state.todo_id}', json=update_data.model_dump())
  assert response.status_code == 200
  assert response.json()['title'] == 'Updated Title'

# Test list before delete so we know that the todos exist
def test_list_todos():
  """Test listing all todo items."""
  response = client.get(url='/todo/list')
  assert response.status_code == 200
  assert isinstance(response.json(), list)
  assert len(response.json()) == 1

def test_delete_todo():
  """Test deleting an existing todo item."""
  response = client.delete(url=f'/todo/delete/{test_state.todo_id}')
  print(response.json())
  assert response.status_code == 200
  assert response.json()['message'] == 'Todo deleted successfully'
