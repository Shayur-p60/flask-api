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

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found", "status": 404}), 404


@app.errorhandler(500)
def internal_error(error):
    logging.exception("Internal server error")
    return jsonify({"error": "Internal server error", "status": 500}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    # Debug stays off unless FLASK_DEBUG is set. The Werkzeug debugger
    # allows code execution, so never enable it on a public host.
    debug = os.getenv("FLASK_DEBUG", "").strip().lower() in ("1", "true", "yes")
    app.run(debug=debug, host="0.0.0.0", port=port)
