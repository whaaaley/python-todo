from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from models import TodoCreate, TodoUpdate, Todo, DeleteResponse, HealthResponse, MessageResponse

app = FastAPI(title='Python Todo API', version='0.1.0')

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    'http://localhost:5001',
    'http://127.0.0.1:5001',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
  ],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

todos = []

@app.get('/hello', response_model=MessageResponse)
async def root():
  return {'message': 'Hello from Python Todo API!'}

@app.post('/todo/create', response_model=Todo)
async def create_todo(todo_data: TodoCreate) -> Todo:
  todo = Todo(
    id=len(todos) + 1,
    title=todo_data.title,
    completed=todo_data.completed,
    created_at=datetime.now()
  )

  todos.append(todo)

  return todo

@app.put('/todo/update/{todo_id}', response_model=Todo)
async def update_todo(todo_id: int, todo_data: TodoUpdate) -> Todo:
  found_item = None

  for todo in todos:
    if todo.id == todo_id:
      found_item = todo
      break

  if not found_item:
    raise HTTPException(status_code=404, detail='Todo item not found')

  # Get only the fields that were actually set in the request
  updates = todo_data.model_dump(exclude_unset=True)

  # Update the Pydantic object directly
  for field, value in updates.items():
    setattr(found_item, field, value)

  return found_item

@app.delete('/todo/delete/{todo_id}', response_model=DeleteResponse)
async def delete_todo(todo_id: int) -> DeleteResponse:
  global todos
  todos = [todo for todo in todos if todo.id != todo_id]
  return {'message': 'Todo deleted successfully'}

@app.get('/todo/list', response_model=List[Todo])
async def list_todos() -> List[Todo]:
  return todos

@app.get('/health', response_model=HealthResponse)
async def health_check():
  return {'status': 'healthy'}

app.mount('/', StaticFiles(directory='dist', html=True), name='static')

def main():
  print('Hello from python-todo!')

if __name__ == '__main__':
  main()
