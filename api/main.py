from fastapi import FastAPI
import redis

app = FastAPI(title="QueueFlow API")

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


@app.get("/")
def root():
    return {"message": "QueueFlow API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/redis-health")
def redis_health():
    redis_client.ping()
    return {"redis": "connected"}

@app.post("/jobs")
def create_job(job: str):
    redis_client.rpush("jobs", job)
    return {"status": "queued", "job": job}




