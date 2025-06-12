.PHONY: dev test install build run stop logs clean db-init db-migrate db-upgrade

dev:
	cd server && uv run uvicorn main:app --reload

install:
	cd server && uv sync

test:
	cd server && PYTHONPATH=. uv run pytest -v -s

db-init:
	cd server && uv run aerich init -t config.TORTOISE_ORM
	cd server && uv run aerich init-db

db-migrate:
	cd server && uv run aerich migrate --name $(name)

db-upgrade:
	cd server && uv run aerich upgrade

build:
	docker build -t python-todo .

run:
	docker run --name python-todo-container -p 8000:8000 python-todo

stop:
	docker stop python-todo-container && docker rm python-todo-container

logs:
	docker logs python-todo-container

clean:
	cd server && rm -rf migrations/
	cd server && rm -f aerich.ini
	docker system prune -f
