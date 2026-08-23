from fastapi import FastAPI

app = FastAPI(title="QueueFlow API")


@app.get("/")
def root():
    return {"message": "QueueFlow API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
