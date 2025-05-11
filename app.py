from flask import Flask, jsonify, Response
import requests

app = Flask(__name__)

API_URL = "https://eleccionesdepartamentales2025.corteelectoral.gub.uy/JSON/ResumenGeneral_P_DPTOS.json"

@app.route("/")
def home():
    return "Servidor proxy funcionando. Usá /api/elecciones"

@app.route("/api/elecciones")
def proxy():
    try:
        resp = requests.get(API_URL, timeout=30)
        resp.raise_for_status()
        return Response(resp.content, status=resp.status_code, content_type="application/json")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
