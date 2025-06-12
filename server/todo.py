from fastapi import APIRouter, HTTPException

import models

router = APIRouter()


@router.post('/create', response_model=models.TodoResponse)
async def create_todo(todo_data: models.TodoCreate) -> models.TodoResponse:
  """Create a new todo item."""

  todo_obj = await models.Todo.create(
    title=todo_data.title, completed=todo_data.completed
  )

  return models.TodoResponse(
    id=todo_obj.id,
    title=todo_obj.title,
    completed=todo_obj.completed,
    created_at=todo_obj.created_at,
  )


@router.put('/update/{todo_id}', response_model=models.TodoResponse)
async def update_todo(
  todo_id: int, todo_data: models.TodoUpdate
) -> models.TodoResponse:
  """Update an existing todo item."""

  todo_obj = await models.Todo.get_or_none(id=todo_id)

  if not todo_obj:
    raise HTTPException(status_code=404, detail='Todo item not found')

  updates = todo_data.model_dump(exclude_unset=True)
  for field, value in updates.items():
    if value is not None:
      setattr(todo_obj, field, value)

  await todo_obj.save()

  return models.TodoResponse(
    id=todo_obj.id,
    title=todo_obj.title,
    completed=todo_obj.completed,
    created_at=todo_obj.created_at,
  )


@router.delete('/delete/{todo_id}', response_model=models.DeleteResponse)
async def delete_todo(todo_id: int) -> models.DeleteResponse:
  """Delete a todo item by ID."""

  todo_obj = await models.Todo.get_or_none(id=todo_id)

  if not todo_obj:
    raise HTTPException(status_code=404, detail='Todo item not found')

  await todo_obj.delete()
  return models.DeleteResponse(message='Todo deleted successfully')


@router.get('/list', response_model=list[models.TodoResponse])
async def list_todos() -> list[models.TodoResponse]:
  """Get all todo items."""

  todo_objs = await models.Todo.all()

  return [
    models.TodoResponse(
      id=todo.id,
      title=todo.title,
      completed=todo.completed,
      created_at=todo.created_at,
    )
    for todo in todo_objs
  ]
