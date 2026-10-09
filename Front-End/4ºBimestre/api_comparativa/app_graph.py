import json
import strawberry
from flask import Flask
from strawberry.flask.views import GraphQLView
 
# Carrega os dados do arquivo JSON único
def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)
 
# Definição dos Tipos GraphQL
@strawberry.type
class Book:
    id: str
    title: str
 
@strawberry.type
class User:
    id: str
    name: str
    email: str
    age: int
 
    @strawberry.field
    def books(self) -> list[Book]:
        data = load_data()
        return [Book(id=b['id'], title=b['title']) for b in data['books'] if b['userId'] == self.id]
 
# Definição da Query
@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: str) -> User | None:
        data = load_data()
        u = next((item for item in data['users'] if item['id'] == id), None)
        if u:
            return User(id=u['id'], name=u['name'], email=u['email'], age=u['age'])
        return None
 
schema = strawberry.Schema(query=Query)
 
# Servidor Flask com interface GraphiQL integrada
app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema, graphiql=True)
)
 
if __name__ == '__main__':
    app.run(port=4000, debug=True)