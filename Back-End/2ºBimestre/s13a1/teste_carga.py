import requests
import time
url = "http://127.0.0.1:5000/recomendacoes"
inicio = time.time()
# Simula 10 acessos seguidos na nossa rota
print("Disparando testes de carga...")
for i in range(10):
    requests.get(url)
    print(f"Requisição {i+1} concluída")
fim = time.time()
print(f"\nTempo total para 10 requisições: {fim - inicio:.2f} segundos")