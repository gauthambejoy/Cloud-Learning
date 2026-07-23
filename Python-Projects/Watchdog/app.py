from flask import Flask, abort, jsonify
import json
import os
import redis
import logging

logging.basicConfig(
    filename="/app/logs/details.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

@app.route("/metrics", methods=["GET"])
def get_metrics():
    try:
        raw_data=redis_client.get("metrics")
        if raw_data is None:
            return jsonify({"Error": "Metrics not found"}), 404
        metrics_obj=json.loads(raw_data)
        logging.info("[FLASK] API has been called and data has been provided as output")
        return jsonify(metrics_obj)
    except redis.exceptions.ConnectionError as e:
        logging.error(f"[FLASK] Redis unavailable: {e}")
        return jsonify({"ERROR" : "REDIS unavailable"}), 503

@app.route("/status", methods=["GET"])
def get_status():
    print(redis.ConnectionError)
    try:
        if redis_client.ping():
            return jsonify({"REDIS" : "Connected"})
    except redis.exceptions.ConnectionError as e:
        print(type(e))
        print(e)
        return jsonify({"REDIS" : "Not Connected"})
        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)