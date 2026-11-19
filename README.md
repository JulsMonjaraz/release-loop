# Release Loop

Small FastAPI service that goes through a complete DevOps cycle:
commit, CI, container image, staging, manual approval, production and monitoring.

## Flow

```mermaid
flowchart LR
    A[Commit / Push] --> B[CI: pytest]
    B --> C[Build Docker image]
    C --> D[Push to GHCR]
    D --> E[Deploy to staging + smoke test]
    E --> F{Manual approval}
    F --> G[Production]
    G --> H[Prometheus + Grafana]
    H --> A
```

## Stack

- Python, FastAPI, pytest
- Docker, GitHub Actions, GitHub Container Registry
- Prometheus and Grafana (via Docker Compose)

## Run locally

```bash
docker compose up --build
```

- API: http://127.0.0.1:8001/health
- Prometheus: http://127.0.0.1:9090
- Grafana: http://127.0.0.1:3000

## Monitoring

![Grafana dashboard](docs/grafana.png)

## What I'd add next

- Real deployment target (Azure Container Apps or Kubernetes)
- Infrastructure as Code with Terraform
- Vulnerability scanning of the image in the pipeline
