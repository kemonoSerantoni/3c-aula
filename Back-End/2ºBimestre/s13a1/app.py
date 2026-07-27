from flask import Flask, request, jsonify
import time
app = Flask(__name__)
# Nosso banco de dados simulado (uma lista na memória)
banco_pedidos = []
@app.post("/pedidos")
def criar_pedido():
    dados = request.get_json()
    novo_pedido = {
        "id": len(banco_pedidos) + 1,
        "produto": dados["produto"],
        "preco": dados["preco"]
    }
    banco_pedidos.append(novo_pedido)
    return jsonify(novo_pedido), 201
@app.get("/pedidos/<int:id_pedido>")
def buscar_pedido(id_pedido):
    for p in banco_pedidos:
        if p["id"] == id_pedido:
            return jsonify(p), 200
    return jsonify({"erro": "Não encontrado"}), 404


cache_dados = None
@app.get("/recomendacoes")
def recomendacoes():
    global cache_dados
# Se o resultado já existe na memória, entrega direto (Leva 0 segundos!)
    if cache_dados:
        return jsonify(cache_dados)
# Se for o primeiro acesso, faz o processo demorado uma única vez
    time.sleep(0.5)
    cache_dados = ["Produto A", "Produto B", "Produto C"]
    return jsonify(cache_dados)