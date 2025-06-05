.PHONY: dev test install

dev:
	cd server && uv run uvicorn main:app --reload

install:
	cd server && uv sync

test:
	cd server && uv run pytest
