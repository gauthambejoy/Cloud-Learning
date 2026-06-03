import psutil
import logging
from flask import Flask, request, jsonify
app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def make_response(data=None, message="success", status=200):
    return jsonify({
        "status": status,
        "message": message,
        "data": data,
    }), status

@app.before_request
def log_request():
    logging.info(f"{request.method} {request.path} from {request.remote_addr}")

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Error occurred: {str(e)}")
    return make_response(message="internal server error", status=500)

@app.route('/cpu')
def cpu():
    cpu_usage=psutil.cpu_percent(interval=1)
    return make_response({ "cpu" : cpu_usage })

@app.route('/memory')
def memory():
    memory_usage=psutil.virtual_memory()
    return make_response({ "total" : memory_usage.total,
             "used" : memory_usage.used,
             "percent" : memory_usage.percent
         })

@app.route('/disk')
def disk():
    disk_usage=psutil.disk_usage("/")
    return make_response({ "total" : disk_usage.total,
             "used" : disk_usage.used,
             "free" : disk_usage.free
         })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)