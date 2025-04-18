from flask import Flask, request, abort

app = Flask(__name__)
latest_script = ""
SECRET_KEY = "7x@K3!-dAqZ9$-LbT#uYvG2Wp*-oF^6NeRs"  # Replace with a strong secret

@app.route('/execute', methods=['POST'])
def execute():
    if request.headers.get("X-Auth") != SECRET_KEY:
        abort(401)  # Unauthorized
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
