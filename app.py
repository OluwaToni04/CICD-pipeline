from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_NAME = os.getenv("APP_NAME", "Deployment Tracker API")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": f"Welcome to {APP_NAME}",
        "status": "running"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "version": APP_VERSION
    })


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "developer": "Oluwatoni Ajaka",
        "role": "Information Technology Student"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)