from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500", "http://parceiro-autrizado.com"])

@app.route("/api/voos", methods=["GET"])
def listar_voos():
    voos = [
        {"id": 1, "origem": "SP", "destino": "RJ", "preço": 100},
        {"id": 2, "origem": "RJ", "destino": "SP", "preço": 200},
        {"id": 3, "origem": "GRU", "destino": "GIG", "preço": 300},
        {"id": 4, "origem": "PIP", "destino": "BCT", "preço": 400},
        {"id": 5, "origem": "PIP", "destino": "CUU", "preço": 500},
    ]
    return jsonify(voos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)