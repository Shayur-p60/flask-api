from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "API is running",
        "status": "success"
    })

@app.route("/status")
def status():
    return jsonify({
        "service": "flask-api",
        "status": "running"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({
        "operation": "addition",
        "result": a + b
    })

if __name__ == "__main__":
    app.run(debug=True)