from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from Kubernetes! Pod: {socket.gethostname()}"

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=8080)
