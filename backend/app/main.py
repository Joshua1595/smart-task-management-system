from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Backend is running successfully"}


@app.get("/health")
def health():
    return {
        "status": "OK",
        "server": "FastAPI",
        "version": "1.0"
    }