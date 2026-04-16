from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest

app = FastAPI()

# 🔥 Metric: total requests count
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")

@app.get("/")
def home():
    REQUEST_COUNT.inc()  # हर request pe +1
    return {"message": "Hello from FastAPI"}

# 📊 Metrics endpoint (Prometheus yaha se data lega)
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")