# 🚀 Dockerized Full-Stack DevOps Project

## 👤 Author

**Aditya Rauniyar**

## 🔗 GitHub Repository

https://github.com/adityarauniyar-ux/fusionpact-devops-challenge

---

## 📌 Project Title

Dockerized Full-Stack Application with CI/CD & Monitoring (Prometheus + Grafana)

---

## 📖 Project Overview

This project demonstrates a complete DevOps implementation of a full-stack application.

It includes:

* Frontend (Nginx)
* Backend (FastAPI - Python)
* Monitoring (Prometheus + Grafana)
* CI/CD (GitHub Actions)

The goal is to:

* Containerize services using Docker
* Automate deployment
* Implement monitoring & observability

---

## 🏗️ Architecture

```
Frontend (Nginx)
        ↓
Backend (FastAPI)
        ↓
   /metrics endpoint
        ↓
   Prometheus
        ↓
    Grafana
```

---

## 🐳 Docker Setup

### Backend Dockerfile

```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend

* Served using **Nginx**
* Port mapping: `3000 → 80`

---

## ⚙️ Docker Compose

```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    container_name: backend_app
    ports:
      - "8000:8000"
    restart: always

  frontend:
    build: ./frontend
    container_name: frontend_app
    ports:
      - "3000:80"
    depends_on:
      - backend
    restart: always

  prometheus:
    image: prom/prometheus
    container_name: prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
    restart: always

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3001:3000"
    restart: always
```

---

## 📊 Monitoring Setup

### Backend Metrics (FastAPI)

```python
from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest

app = FastAPI()

REQUEST_COUNT = Counter("app_requests_total", "Total API Requests")

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "API is running successfully"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

---

### Prometheus Configuration

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "backend_service"
    static_configs:
      - targets: ["backend:8000"]
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Build Docker Images
        run: docker-compose build

      - name: Start Containers
        run: docker-compose up -d
```

---

## 💾 Data Persistence Strategy

* Docker volumes for service isolation
* Prometheus stores metrics locally
* Grafana dashboards stored in container volumes
* Backend is stateless (scalable)

---

## ▶️ How to Run

```bash
docker-compose up --build
```

Check running containers:

```bash
docker ps
```

View logs:

```bash
docker logs backend_app
```

---

## 🌐 Application URLs

| Service     | URL                           |
| ----------- | ----------------------------- |
| Backend API | http://localhost:8000         |
| Metrics     | http://localhost:8000/metrics |
| Prometheus  | http://localhost:9090         |
| Grafana     | http://localhost:3001         |

### Grafana Login

```
Username: admin
Password: admin
```

---

## ✅ Verification

* Backend running ✔️
* Metrics exposed ✔️
* Prometheus scraping ✔️
* Grafana dashboard working ✔️

---

## 📚 Key Learnings

* Docker containerization
* Multi-container setup using Docker Compose
* Monitoring with Prometheus & Grafana
* CI/CD using GitHub Actions
* Real-world DevOps workflow

---

## 🏁 Final Summary

This project demonstrates a production-ready DevOps pipeline with:

* Full-stack architecture
* Monitoring & observability
* CI/CD automation

The system is scalable, containerized, and ready for deployment.

---

## 📸 Screenshots
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/a925b17b-a0d8-4cfa-953f-ad6b93f81a88" />
<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/9dad9fcc-3aff-48b9-8483-2feba1e5844a" />



