from models import TodoCreate, TodoUpdate
from fastapi.testclient import TestClient
from main import app
from polyfactory.factories.pydantic_factory import ModelFactory

client = TestClient(app)
todo_id = 0

class TodoCreateFactory(ModelFactory[TodoCreate]):
  __use_examples__ = True

def test_create_todo():
  global todo_id
  fake_todo_create = TodoCreateFactory.build()
  response = client.post(url='/todo/create', json=fake_todo_create.model_dump())
  todo_id = response.json()['id']
  assert response.status_code == 200

def test_update_todo():
  update_data = TodoUpdate(title='Updated Title')
  response = client.put(url=f'/todo/update/{todo_id}', json=update_data.model_dump())
  assert response.status_code == 200
  assert response.json()['title'] == 'Updated Title'

# Test list before delete so we know that the todos exist
def test_list_todos():
  response = client.get(url='/todo/list')
  assert response.status_code == 200
  assert isinstance(response.json(), list)
  assert len(response.json()) == 1

def test_delete_todo():
  response = client.delete(url=f'/todo/delete/{todo_id}')
  print(response.json())
  assert response.status_code == 200
  assert response.json()['message'] == 'Todo deleted successfully'
