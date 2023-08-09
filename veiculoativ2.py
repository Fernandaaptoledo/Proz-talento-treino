rodas = 0
peso = 0
qtd_pessoas = 0

def cnh_category(rodas, peso=0, pessoas=0):
    if 2 <= rodas <= 3:
        return print("A")
    elif rodas >= 4:
        if pessoas <= 5 and peso <= 3500:
            return print("B")
        elif pessoas > 8:
            return print("D")
        elif peso <= 6000:
            return print("C")
        elif peso > 6000:
            return print("E")
    else:
        return print("Erro de entrada de dados")


cnh_category(4, 4000, 7)