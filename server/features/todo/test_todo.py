"""
Test suite for the Todo API.

This module contains integration tests for all Todo API endpoints including
create, read, update, and delete operations using FastAPI TestClient.
"""

import os
from typing import Any

import pytest
from fastapi.testclient import TestClient
from polyfactory.factories.pydantic_factory import ModelFactory
from tortoise import Tortoise

from features.todo.todo_schemas import TodoCreate, TodoUpdate

os.environ['TESTING'] = '1'

TEST_TORTOISE_ORM: dict[str, Any] = {
  'connections': {'default': 'sqlite://:memory:'},
  'apps': {'models': {'models': ['models'], 'default_connection': 'default'}},
}


class TestState:
  """Container for test state."""

  todo_id = 0


test_state = TestState()


class TodoCreateFactory(ModelFactory[TodoCreate]):
  """Factory for generating TodoCreate test instances."""

  __use_examples__ = True


@pytest.fixture(scope='module', autouse=True)
async def setup_database():
  """Set up and tear down the test database."""
  await Tortoise.init(config=TEST_TORTOISE_ORM)
  await Tortoise.generate_schemas()
  yield
  await Tortoise.close_connections()


# Import app after setting up the test database
from main import app

client = TestClient(app)


def test_create_todo():
  """Test creating a new todo item."""
  fake_todo_create = TodoCreateFactory.build()
  response = client.post(url='/todo/create', json=fake_todo_create.model_dump())
  test_state.todo_id = response.json()['id']
  assert response.status_code == 200


def test_update_todo():
  """Test updating an existing todo item."""
  update_data = TodoUpdate(title='Updated Title')
  response = client.put(
    url=f'/todo/update/{test_state.todo_id}', json=update_data.model_dump()
  )
  assert response.status_code == 200
  assert response.json()['title'] == 'Updated Title'


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
