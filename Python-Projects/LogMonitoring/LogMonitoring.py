from flask import Flask, request, jsonify

app = Flask(__name__)

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
    result=monitor(filepath)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)