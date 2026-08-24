# QueueFlow

QueueFlow is a simple background job processing application I built using FastAPI, Redis and Python.

The API receives jobs and sends them to a Redis queue. A separate worker takes jobs from the queue and processes them.

I containerized the services with Docker and deployed them using Kubernetes and Helm. I also added a GitHub Actions workflow to automatically check the project when changes are pushed.

## Tech Stack

- Python
- FastAPI
- Redis
- Docker
- Kubernetes
- Helm
- GitHub Actions

## Architecture

```text
Client
  |
  v
FastAPI API
  |
  v
Redis Queue
  |
  v
Worker
```

## Running the Project

Using Docker Compose:

```bash
docker compose up --build
```

Test the API:

```bash
curl http://localhost:8000/health
```

Submit a job:

```bash
curl -X POST "http://localhost:8000/jobs?job=test-job"
```

## Kubernetes

The Kubernetes manifests are stored in the `k8s/` directory.

```bash
kubectl apply -f k8s/
kubectl get pods
```

## Helm

The Helm chart is stored in `queueflow-chart/`.

```bash
helm lint queueflow-chart
helm install queueflow queueflow-chart
```

## CI

The GitHub Actions workflow checks Python syntax, builds the Docker images, and validates the Helm chart whenever changes are pushed to the repository.
