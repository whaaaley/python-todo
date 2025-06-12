"""
Test suite for the Health API.

This module contains tests for the health check endpoint.
"""

import os
from typing import Any

import pytest
from fastapi.testclient import TestClient
from tortoise import Tortoise

os.environ['TESTING'] = '1'

TEST_TORTOISE_ORM: dict[str, Any] = {
  'connections': {'default': 'sqlite://:memory:'},
  'apps': {'models': {'models': ['models'], 'default_connection': 'default'}},
}


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


def test_health_check():
  """Test the health check endpoint."""
  response = client.get(url='/health/status')
  assert response.status_code == 200
  assert response.json()['status'] == 'healthy'
