# FastAPI Docker Image Action

A FastAPI app with automated tests, containerized with Docker, and built and pushed to Docker Hub by GitHub Actions.

## Routes
- `/` returns a hello message
- `/health` returns `{"status":"healthy"}`
- `/students` returns a list of students

## Run locally with Docker Compose
```
docker compose up --build
```
Then open http://localhost:8000/health

## Run the image from Docker Hub
```
docker pull kanikaagarwal006/fastapi-app:v0.1
docker run --rm -p 8000:8000 kanikaagarwal006/fastapi-app:v0.1
```
On Apple Silicon Macs, add `--platform linux/amd64` to both commands.

## CI/CD
On every push to `main`, GitHub Actions installs dependencies, starts the server, runs `automationTesting.py`, then builds and pushes the image to Docker Hub.

Docker Hub: https://hub.docker.com/r/kanikaagarwal006/fastapi-app