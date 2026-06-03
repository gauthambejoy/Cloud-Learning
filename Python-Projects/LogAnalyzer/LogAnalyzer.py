from flask import Flask
from dotenv import load_dotenv
import subprocess
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")

def printlog(keyword=None):
    log_command = os.getenv("LOG_COMMAND", "journalctl") 
    result=subprocess.run([log_command], capture_output=True, text=True)
    logs = result.stdout.splitlines()
    if keyword:
         logs = [line for line in logs if keyword in line]
    return "<pre>" + "\n".join(logs) + "</pre>"

@app.route("/error")
def error_log():
    return printlog("ERROR")

@app.route("/warning")
def warning_log():
     return printlog("WARNING")

@app.route("/info")
def info_log():
     return printlog("INFO")              

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("DEBUG", "False") == "True"

    app.run(host="0.0.0.0",port=port, debug=debug)