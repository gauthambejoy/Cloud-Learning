from flask import Flask, request, jsonify
import redis
import json
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True
)

def monitor(logfile):
    try:
        with open(logfile, 'r') as f:
            info_count=0
            error_count=0
            warning_count=0
            total_lines=0
            for line in f:
                lines=line.lower()
                total_lines+=1
                if "info" in lines:
                    info_count+=1
                if "error" in lines:
                    error_count+=1
                if "warning" in lines:
                    warning_count+=1
            return {
                "TOTAL LINES": total_lines,
                "INFO": info_count,
                "ERROR": error_count,
                "WARNING": warning_count
            }      
    except FileNotFoundError:
            print("No such file or directory, please enter the proper file name")

@app.route("/upload",methods=["POST"])        
def upload():
    file = request.files["file"]

    filepath = f"uploads/{file.filename}"
    file.save(filepath)

    cache_key = file.filename
    cached = redis_client.get(cache_key)

    if cached:
        return jsonify({
            "source": "cache",
            "result": json.loads(cached)
        })
    result=monitor(filepath)

    redis_client.set(
        cache_key,
        json.dumps(result),
        ex=60
    )

    return jsonify({
        "source": "system",
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)