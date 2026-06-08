arquivo = open("bios.txt","r")

bio = arquivo.read()
arquivo.close()

print()

print("autenticacao Biometrica")


biometria = input("coloque sua biometria: ")

if biometria.upper() == bio.upper:
    print("Biometria validada")

else:
    print("Biometria invalida")