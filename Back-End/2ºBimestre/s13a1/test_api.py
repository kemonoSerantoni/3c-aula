from app import app
def test_fluxo_de_pedidos():
    cliente = app.test_client()
# Cenário 1: Enviar um pedido para a API
    res_post = cliente.post("/pedidos", json={"produto": "Teclado Gamer", "preco": 150})

    assert res_post.status_code == 201
    assert res_post.get_json()["id"] == 1
# Cenário 2: Tentar buscar o pedido que acabamos de criar
    res_get = cliente.get("/pedidos/1")
    assert res_get.status_code == 200
    assert res_get.get_json()["produto"] == "Teclado Gamer"

