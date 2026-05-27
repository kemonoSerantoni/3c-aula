from flask import Flask
from strawberry.flask.views import GraphQLView
import graphene
import json
 
# =========================
# Funções JSON
# =========================
 
def carregar():
    with open("produtos.json", "r") as f:
        return json.load(f)
 
def salvar(dados):
    with open("produtos.json", "w") as f:
        json.dump(dados, f, indent=2)
 
# =========================
# Flask
# =========================
 
app = Flask(__name__)
 
# =========================
# Tipo Produto
# =========================
 
class Produto(graphene.ObjectType):
    id = graphene.Int()
    nome = graphene.String()
 
# =========================
# Queries
# =========================
 
class Query(graphene.ObjectType):
 
    # Lista todos
    produtos = graphene.List(Produto)
 
    # Busca por ID
    produto = graphene.Field(
        Produto,
        id=graphene.Int(required=True)
    )
 
    # Resolver lista
    def resolve_produtos(root, info):
        return carregar()
 
    # Resolver único
    def resolve_produto(root, info, id):
 
        produtos = carregar()
 
        for produto in produtos:
            if produto["id"] == id:
                return produto
 
        return None
 
# =========================
# Mutation adicionar
# =========================
 
class AdicionarProduto(graphene.Mutation):
 
    class Arguments:
        nome = graphene.String(required=True)
 
    ok = graphene.Boolean()
    produto = graphene.Field(Produto)
 
    def mutate(root, info, nome):
 
        produtos = carregar()
 
        novo = {
            "id": len(produtos) + 1,
            "nome": nome
        }
 
        produtos.append(novo)
 
        salvar(produtos)
 
        return AdicionarProduto(
            ok=True,
            produto=novo
        )
 
# =========================
# Mutation deletar
# =========================
 
class DeletarProduto(graphene.Mutation):
 
    class Arguments:
        id = graphene.Int(required=True)
 
    ok = graphene.Boolean()
 
    def mutate(root, info, id):
 
        produtos = carregar()
 
        for produto in produtos:
 
            if produto["id"] == id:
 
                produtos.remove(produto)
 
                salvar(produtos)
 
                return DeletarProduto(ok=True)
 
        return DeletarProduto(ok=False)
 
# =========================
# Classe Mutation
# =========================
 
class Mutation(graphene.ObjectType):
 
    adicionar_produto = AdicionarProduto.Field()
 
    deletar_produto = DeletarProduto.Field()
 
# =========================
# Schema
# =========================
 
schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
 
# =========================
# Rotas
# =========================
 
@app.route("/")
def home():
    return "GraphQL funcionando"
 
app.add_url_rule(
    "/graphql",
view_func=GraphQLView.as_view(
    "graphql_view",
    schema=schema,
),
    )
 
 
# =========================
# Main
# =========================
 
if __name__ == "__main__":
    app.run(debug=True)
 