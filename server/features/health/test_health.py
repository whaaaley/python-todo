"""
Test suite for the Health API.

This module contains tests for the health check endpoint.
"""

import asyncio
import os
from typing import Any

from fastapi.testclient import TestClient
from tortoise import Tortoise

os.environ['TESTING'] = '1'

TEST_TORTOISE_ORM: dict[str, Any] = {
  'connections': {'default': 'sqlite://:memory:'},
  'apps': {'models': {'models': ['models'], 'default_connection': 'default'}},
}


# Set up Tortoise before importing the app
async def setup_tortoise():
  """Initialize Tortoise ORM for testing."""
  await Tortoise.init(config=TEST_TORTOISE_ORM)
  await Tortoise.generate_schemas()


asyncio.run(setup_tortoise())

# Import app after setting up the test database
from main import app

client = TestClient(app)


def test_health_check():
  """Test the health check endpoint."""
  response = client.get(url='/health/status')
  assert response.status_code == 200
  assert response.json()['status'] == 'healthy'
