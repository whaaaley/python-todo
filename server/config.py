"""
Tortoise ORM configuration for Aerich migrations.
"""

import os
from typing import Any

TORTOISE_ORM: dict[str, Any] = {
  'connections': {
    'default': os.getenv(
      'DATABASE_URL', 'postgres://postgres:postgres@localhost:5432/python_todo'
    )
  },
  'apps': {
    'models': {
      'models': ['models', 'aerich.models'],
      'default_connection': 'default',
    },
  },
}
