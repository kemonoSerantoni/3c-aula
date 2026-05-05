from flask import Flask, jsonify, request
import json
app = Flask(__name__)

#func ler arquivo json
def carregar_turma():
    with open("turma.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados

def salvar_turma(turma):
    with open("turma.json", "w") as arquivo:
        json.dump(turma, arquivo, indent=4)



@app.route("/")
def home():
    return "API do 3c funcionamento"
@app.route("/alunos")
def listar_alunos():
    turma = carregar_turma()
    return jsonify(turma)


@app.route("/alunos/<nome>")
def buscar_aluno(nome):
    turma = carregar_turma()
    for aluno in turma:
        if aluno["nome"].lower() == nome.lower():
            return jsonify(aluno)
    return{"erro":" Aluno é um merda e não existe"}


@app.route("/alunos/<int:id>")
def buscar_aluno_id(id):
    turma = carregar_turma()
    for aluno in turma:
        if aluno["id"] == id:
            return jsonify(aluno)
    return jsonify({"erro":" Aluno é um merda e não existe"})

@app.route("/adicionar/<nome>/<int:idade>")
def adicionar_aluno(nome,idade):
    turma = carregar_turma()
    novo_id = len(turma) + 1
    novo_aluno = {
        "id": novo_id,
        "nome": nome,
        "idade": idade
    }
    turma.append(novo_aluno)
    salvar_turma(turma)
    return jsonify({
        "mensagem:": "Aluno adicionado",
        "aluno": novo_aluno
    })

@app.route("/remover/<int:id>")
def remover_aluno(id):
    turma = carregar_turma()
    for aluno in turma:
        if aluno["id"] == id:
            turma.remove(aluno)
            salvar_turma(turma)
            return jsonify({
                "mensagem": "aluno removido",
                "aluno": aluno
            })
    return jsonify({"erro": "aluno nao encontrado"})


@app.route("/adicionar/alunos/form", methods=["post"])
def adicionar():
    turma = carregar_turma()
    nome = request.form["nome"]
    idade = int(request.form["idade"])
    novo_id = len(turma) + 1
    novo_aluno = {
       "id": novo_id,
       "nome": nome,
       "idade": idade 
    }
    turma.append(novo_aluno)
    salvar_turma(turma)
    return jsonify({
        "mensagem": "Aluno Adicionado via form",
        "Aluno": novo_aluno
    })

#Teste de função deletar
@app.route("/deletar/alunos/form", methods=["delete"])
def deletar():
    turma = carregar_turma()
    a_id = int(request.form["id"])
    for aluno in turma:
        if aluno["id"] == a_id:
            turma.remove(aluno)
            salvar_turma(turma)
            return jsonify({
                "mensagem": "aluno removido pelo form",
                "aluno": aluno
            })
        return jsonify({"erro": "aluno nao encontrado"})
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
