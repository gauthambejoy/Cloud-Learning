import redis
import os
import time
import json
import logging
from monitor import monitor

logging.basicConfig(
    filename="/app/logs/details.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)
redis_key="metrics"
logging.info("[WATCDOG] Watchdog has started")
while True:
    metrics=monitor()
    redis_client.set(
        redis_key,
        json.dumps(metrics),
        ex=60
    )
    logging.info("[WATCHDOG] Data is cached")
    time.sleep(5)