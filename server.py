from flask import Flask, request, abort

app = Flask(__name__)

# Replace with your secret key
SECRET_KEY = "7x@K3!-dAqZ9$-LbT#uYvG2Wp*-oF^6NeRs"
latest_script = ""

@app.route('/execute', methods=['POST'])
def execute():
    # Check if the authorization header matches the secret key
    if request.headers.get("X-Auth") != SECRET_KEY:
        abort(401)  # Unauthorized
    global latest_script
    latest_script = request.data.decode('utf-8')
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
