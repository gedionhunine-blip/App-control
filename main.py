
import os
import uuid
from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ethiopian AI Video")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

jobs = {}

@app.get("/")
def home():
    return {"message": "Ethiopian AI Video Backend is running"}

@app.get("/api/health")
def health():
    return {"status": "online"}

@app.post("/api/generate")
def generate(prompt: str = Form(...)):
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")

    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "status": "queued",
        "prompt": prompt
    }

    return {
        "job_id": job_id,
        "status": "queued",
        "message": "Request received"
    }

@app.get("/api/status/{job_id}")
def status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]
