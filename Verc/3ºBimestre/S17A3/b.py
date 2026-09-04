def calcular_total(valor, taxa):
    if valor < 0:
        return 0
    return valor + (valor * taxa)
