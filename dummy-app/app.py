from flask import Flask, Response
from prometheus_client import Counter, generate_latest
import time
import threading
import random

app = Flask(__name__)
requests_total = Counter('dummy_requests_total', 'Total dummy requests')

def log_writer():
    while True:
        print(f"[DUMMY-APP] Message at {time.strftime('%H:%M:%S')}")
        time.sleep(2)

@app.route("/")
def index():
    requests_total.inc()
    return "Dummy App Running!\n"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    threading.Thread(target=log_writer, daemon=True).start()
    app.run(host="0.0.0.0", port=8000)
