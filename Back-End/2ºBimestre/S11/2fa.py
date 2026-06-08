import random
codigo = random.randint(
    100000,
    999999 
)

print(
    "\nCodigo enviado: ",
    codigo
)

codigo_digitado = int(input("digite o codigo recebido: "))

if codigo_digitado == codigo:
    print("Codigo Valido")
else:
    print("Codigo INVALIDO")