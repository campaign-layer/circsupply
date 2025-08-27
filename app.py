from flask import Flask, jsonify, Response
import time

app = Flask(__name__)

TOTAL_SUPPLY = 10_000_000_000  # 10 billion
CIRC_PERCENT = 0.21
CIRC_SUPPLY = int(TOTAL_SUPPLY * CIRC_PERCENT)

@app.get("/supply.json")
def supply_json():
    payload = {
        "circulating_supply": str(CIRC_SUPPLY),
        "total_supply": str(TOTAL_SUPPLY),
        "last_updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    return jsonify(payload)

@app.get("/circulating-supply")
def supply_plain():
    return Response(str(CIRC_SUPPLY), mimetype="text/plain")

@app.get("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
