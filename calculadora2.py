def calculadora(num1, num2, op):
    calculo = 0
    if (op == 1):
        calculo = num1 + num2
    elif (op == 2):
        calculo = num1 - num2
    elif (op == 3):
        calculo = num1 * num2
    elif (op == 4 and num2 != 0):
        calculo = num1 / num2
    return calculo

TEXTO_MENU = """
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
0. Sair
"""

while (True):
    op = int(input(f"""Selecione a operação: {TEXTO_MENU}""")) 
    if (op == 0):
        break
    
    num1 = int(input("Digite o primeiro número: ")) 
    num2 = int(input("Digite o segundo número: ")) 

    resultado = calculadora(num1, num2, op)
    print("Resultado: ", resultado)