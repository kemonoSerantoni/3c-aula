import json
from flask import Flask, jsonify
 
app = Flask(__name__)
 
# Carrega os dados do arquivo JSON único
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)
 
# Endpoint 1: Retorna dados do usuário (retorna tudo, mesmo se você só quiser o nome)
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    data = load_data()
    user = next((u for u in data['users'] if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user)
 
# Endpoint 2: Retorna os livros de um usuário específico
@app.route('/users/<user_id>/books', methods=['GET'])
def get_user_books(user_id):
    data = load_data()
    books = [b for b in data['books'] if b['userId'] == user_id]
    return jsonify(books)
 
if __name__ == '__main__':
    app.run(port=3000, debug=True)