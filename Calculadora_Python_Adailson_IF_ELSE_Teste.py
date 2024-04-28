
#int bool str chr

def soma(a, b):
    return (a+b)

def multiplicacao(a, b):
    return (a*b)

def divisao(a, b):
    return (a/b)

def subtracao(a, b):
    return (a-b)

print("\n\033[0;34;40m**Bem vindo à Calculadora em Python**\n \033[m")

def calculadora():    

    print("Selecione a Operação:\n\n A - Soma\n B - Multiplicação\n C - Divisão\n D - Subtração\n")
    operacao = input().lower()

    while((operacao != 'a' ) and (operacao != 'b') and (operacao != 'c') and (operacao != 'd')):
        print("Selecione a alternativa A, B, C ou D")
        operacao = input().lower()

    num1 = float(input("Insira o primeiro Número: \n"))
    num2 = float(input("Insira o segundo Número: \n"))

    if(operacao == 'a'):{ 
        print(f"\nO Resultado da soma de \033[0;32;40m{num1}\033[m + \033[0;34;40m{num2}\033[m é: \033[0;33;40m{soma(num1,num2)}\033[m")
    }
    elif(operacao == 'b'):{
        print(f"\nO Resultado da multiplicação de \033[0;32;40m{num1}\033[m x \033[0;34;40m{num2}\033[m é: \033[0;33;40m{multiplicacao(num1,num2)}\033[m")
    }
    elif(operacao == 'c'):{
        print(f"\nO Resultado da divisão de \033[0;32;40m{num1}\033[m / \033[0;34;40m{num2}\033[m é: \033[0;33;40m{divisao(num1,num2)}\033[m")
    }
    elif(operacao == 'd'):{
        print(f"\nO Resultado da subtração de \033[0;32;40m{num1}\033[m - \033[0;34;40m{num2}\033[m é: \033[0;33;40m{subtracao(num1,num2)}\033[m")
    }
    
    print('\nDeseja fazer mais um calculo? S/N:\n')
    reinicia = input().lower()

    while((reinicia != 's') and (reinicia != 'n')):
        print('\nEscolha "S" para SIM e "N" para Não:\n')
        reinicia = input().lower()
    if(reinicia == "s"):{
        calculadora()
    }
    else: print("Calculadora Finalizada")
        


calculadora()