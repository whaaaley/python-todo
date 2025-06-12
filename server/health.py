from fastapi import APIRouter

import models

router = APIRouter()

@router.get('/', response_model=models.MessageResponse)
async def root():
  """Return a simple hello message."""
  return {'message': 'Hello from Python Todo API!'}

@router.get('/hello', response_model=models.MessageResponse)
async def hello():
  """Return a simple hello message."""
  return {'message': 'Hello from Python Todo API!'}

@router.get('/health', response_model=models.HealthResponse)
async def health_check():
  """Health check endpoint."""
  return {'status': 'healthy'}
