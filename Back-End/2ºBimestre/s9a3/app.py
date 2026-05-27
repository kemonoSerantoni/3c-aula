from flask import Flask, request, jsonify
import json
from functools import wraps

 
app = Flask(__name__)
 
# =========================
# JSON
# =========================
 
def carregar():
    with open("produtos.json", "r") as f:
        return json.load(f)
 
def salvar(dados):
    with open("produtos.json", "w") as f:
        json.dump(dados, f, indent=2)
 
# =========================
# HOME
# =========================
 
@app.route("/")
def home():
    return "API segura funcionando"
 
# =========================
# LOGIN
# =========================
 
@app.route("/login", methods=["POST"])
def login():
 
    dados = request.get_json()
 
    if dados["user"] == "admin" and dados["senha"] == "123":
 
        return {
            "token": "abc123"
        }
 
    return {
        "erro": "login inválido"
    }, 401
 
# =========================
# PROTEÇÃO
# =========================
 
def proteger(f):
 
    @wraps(f)
    def wrapper(*args, **kwargs):
 
        token = request.headers.get("token")
 
        if token != "abc123":
 
            return {
                "erro": "acesso negado"
            }, 403
 
        return f(*args, **kwargs)
 
    return wrapper
 
# =========================
# LISTAR PRODUTOS
# =========================
 
@app.route("/produtos")
@proteger
def listar():
 
    return jsonify(carregar())
 
# =========================
# ADICIONAR
# =========================
 
@app.route("/produtos", methods=["POST"])
@proteger
def adicionar():
 
    produtos = carregar()
 
    dados = request.get_json()
 
    novo = {
        "id": len(produtos) + 1,
        "nome": dados["nome"]
    }
 
    produtos.append(novo)
 
    salvar(produtos)
 
    return novo
 
# =========================
# DELETE
# =========================
 
@app.route("/produtos/<int:id>", methods=["DELETE"])
@proteger
def deletar(id):
 
    produtos = carregar()
 
    for p in produtos:
 
        if p["id"] == id:
 
            produtos.remove(p)
 
            salvar(produtos)
 
            return {
                "msg": "removido"
            }
 
    return {
        "erro": "não encontrado"
    }
 
# =========================
 
if __name__ == "__main__":
    app.run(debug=True)
