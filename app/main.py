import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(
    title="KubeResilience Demo Service",
    description="A workload for Kubernetes resilience experiments.",
    version="0.1.0",
)

STARTED_AT = datetime.now(timezone.utc).isoformat()

POD_NAME = os.getenv("POD_NAME", socket.gethostname())
POD_NAMESPACE = os.getenv("POD_NAMESPACE", "default")
POD_NODE_NAME = os.getenv("POD_NODE_NAME", "unknown")


@app.get("/")
def index():
    return {
        "service": "kube-resilience-demo",
        "message": "KubeResilience Lab is running",
        "pod": POD_NAME,
        "namespace": POD_NAMESPACE,
        "node": POD_NODE_NAME,
        "started_at": STARTED_AT,
    }


@app.get("/health/live")
def liveness():
    return {
        "status": "alive",
        "pod": POD_NAME,
    }


@app.get("/health/ready")
def readiness():
    return {
        "status": "ready",
        "pod": POD_NAME,
    }


@app.get("/metadata")
def metadata():
    return {
        "pod": POD_NAME,
        "namespace": POD_NAMESPACE,
        "node": POD_NODE_NAME,
        "hostname": socket.gethostname(),
        "started_at": STARTED_AT,
    }