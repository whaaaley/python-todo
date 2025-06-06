.PHONY: dev test install build run stop logs clean

dev:
	cd server && uv run uvicorn main:app --reload

install:
	cd server && uv sync

test:
	cd server && uv run pytest test_main.py -v -s

build:
	docker build -t python-todo .

run:
	docker run --name python-todo-container -p 8000:8000 python-todo

stop:
	docker stop python-todo-container && docker rm python-todo-container

logs:
	docker logs python-todo-container
