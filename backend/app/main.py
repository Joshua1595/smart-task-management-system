from fastapi import FastAPI

app = FastAPI(
    title="Smart Task Management API",
    description="Backend API for the Smart Task Management System",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Smart Task Management API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }