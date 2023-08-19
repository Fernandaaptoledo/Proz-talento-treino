def calculadora(num1, op, num2):
    if op == "+" : return num1 + num2

    elif op == "-": return num1 - num2

    elif op == "*": return num1 * num2

    elif op == "/": return num1 / num2

    else : return 0

num1=int(input("Digite um número: "))

op=str(input("Digite um operador: "))

num2=int(input("Digite um número: "))

resultado=(calculadora(num1, op, num2))
print(resultado)