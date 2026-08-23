import redis
redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True,
    socket_timeout=None
)



print("QueueFlow Worker started.")
print("Waiting for jobs...")

while True:
    _, job = redis_client.blpop("jobs", timeout=0)
    print(f"Processing job: {job}")

