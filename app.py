import os
import time
import redis
from flask import Flask

app = Flask(__name__)

# Connect to the Redis service by its service name in Docker Compose
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"Hello Saira (Roll: 55503)! This page has been visited {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)