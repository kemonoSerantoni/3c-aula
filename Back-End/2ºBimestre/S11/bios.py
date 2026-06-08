import bcrypt
biometria = input("adicione sua biometria (uma letra): ")



arquivo = open("bios.txt", "w")
arquivo.write(
    biometria
)

arquivo.close()

print("biometria adicionada")