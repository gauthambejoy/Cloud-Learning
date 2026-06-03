import psutil
import logging
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify, request

app=Flask(__name__)

logging.basicConfig(
    filename="SystemMonitoring.log",
    encoding='utf-8',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
    )

def make_response(data=None, message="success", status=200):
    return jsonify({
        "data": data,
        "message": message,
        "status": status
    }), status

@app.before_request
def log_request():
    logging.info(f"{request.method},{request.path} from {request.remote_addr}")

@app.errorhandler(Exception)
def error_handling(e):
    if isinstance(e, HTTPException):
        logging.warning(f"HTTP ERROR {e.code}: {e.description}")
        return make_response(
            message= e.description,
            status= e.code
        )
    logging.error(f"Error occured: {str(e)}")
    return make_response(message="Internal Server Error", status=500)

@app.route("/health")
def health():
    return make_response({
        "services": "healthy"
    })

@app.route("/cpu")
def cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return make_response({
        "cpu": cpu_usage
    })

@app.route("/memory")
def memory():
    memory_usage = psutil.virtual_memory()
    return make_response({
        "total": memory_usage.total, 
        "used": memory_usage.used,
        "free": memory_usage.free
    })
@app.route("/disk")
def disk_usage():
    disk_usage = psutil.disk_usage("/")
    return make_response({
        "total": disk_usage.total,
        "used": disk_usage.used,
        "available": disk_usage.free,
        "percent": disk_usage.percent
    })

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)