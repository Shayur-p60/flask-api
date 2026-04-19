import logging
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    logging.info("Home endpoint called")
    return jsonify({
        "message": "API is running",
        "status": "success"
    })

@app.route("/status")
def status():
    logging.info("Status endpoint checked")
    return jsonify({
        "service": "flask-api",
        "status": "running"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return jsonify({
        "operation": "addition",
        "result": a + b
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)