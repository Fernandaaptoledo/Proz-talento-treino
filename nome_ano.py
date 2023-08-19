nomeCompleto = input("Digite seu nome?")

identif = True

while(identif == True):
    print("Digite seu ano de nascimento")
    try:
        anoNascimento = int(input())
        if (anoNascimento < 1922) or (anoNascimento > 2021):
            print("Digite um ano de nascimento entre 1922 e 2021")
        else:
            idade = 2021 - anoNascimento
            print("Seu nome é: ", nomeCompleto, "sua idade é: ", idade, "anos")

            identif = False
    except:
        print("Digite o ano do seu nascimento em números e dentro do intervalo por favor")

    

