from flask import Flask, request

app = Flask(__name__)
latest_script = ""

@app.route('/execute', methods=['POST'])
def execute():
    global latest_script
    latest_script = request.data.decode('utf-8')  # Store the script received in the POST request
    return "OK"

@app.route('/getscript', methods=['GET'])
def get_script():
    return latest_script or ""  # Return the latest script sent via the /execute endpoint

@app.route('/')
def home():
    return "Flask executor server is running."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)  # Running on all addresses, port 8080
