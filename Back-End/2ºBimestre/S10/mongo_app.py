from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://luccaserantonipinto:Lucca2002113@cluster0.lpg8x2i.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client['escola']
coleção = db['alunos']
aluno = {
    "nome": "Enzo",
    "idade": 4,
    "turma": "prezinho",
    "notas": [4, 7, 10, 10, 1],
    "cidade": "Parana"
}
resultado = coleção.insert_one(aluno)
print(f"Aluno cadastrado com sucesso! com id:{resultado.inserted_id}")