import time


def process_jobs():
    print("QueueFlow Worker started.")

    while True:
        print("Worker is checking for new jobs...")
        time.sleep(5)


if __name__ == "__main__":
    process_jobs()
