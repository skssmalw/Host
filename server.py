from flask import Flask, request, abort
import os  # Needed for accessing environment variables

app = Flask(__name__)
latest_script = ""
SECRET_KEY = "7x@K3!-dAqZ9$-LbT#uYvG2Wp*-oF^6NeRs"  # Replace with a strong secret

@app.route('/execute', methods=['POST'])
def execute():
    if request.headers.get("X-Auth") != SECRET_KEY:
        abort(401)
    global latest_script
    latest_script = request.data.decode('utf-8')
    return "OK"

@app.route('/getscript', methods=['GET'])
def get_script():
    if request.headers.get("X-Auth") != SECRET_KEY:
        abort(401)
    return latest_script or ""

@app.route('/')
def home():
    return "Flask executor server is running."

# Bind to the correct port for Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
