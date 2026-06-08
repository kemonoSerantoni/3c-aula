import bcrypt
arquivo = open("usuarios.txt","r")

dados = arquivo.read()
arquivo.close()

usuario_salvo, hash_salvo = dados.split(";")

usuario = input("Usuario: ")
senha = input("Senha: ")

if usuario == usuario_salvo:
    valido = bcrypt.checkpw(
    senha.encode(),
    hash_salvo.encode()
    )

    if valido:
        print("Senha correta")
    else:
        print("Senha incorreta")

else:
    print("Usuario não encontrado")