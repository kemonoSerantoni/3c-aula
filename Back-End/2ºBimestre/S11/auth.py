import bcrypt
usuario = input("digite o nome do usuario: ")
senha = input("digite a senha: ")

hash_senha = bcrypt.hashpw(
    senha.encode(),
    bcrypt.gensalt()
)


arquivo = open("usuarios.txt", "w")
arquivo.write(
    usuario + ";" +
    hash_senha.decode()
)

arquivo.close()

print("usuario cadastrado")