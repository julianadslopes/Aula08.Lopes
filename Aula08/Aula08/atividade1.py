import os
import random

def limpa_tela():
    os.system ("cls")

def decoracao():
    print(100*"=")    

def soma (a,b):
    mais = a + b
    return mais

def subtracao (a,b):
    menos = a - b
    return menos

def multiplicacao (a,b):
    vezes = a * b
    return vezes

def divisao (a,b):
    dividido = a / b
    return dividido

def gera_numeros (inicio, final, quantidade):
    return [random.randint(inicio, final) for i in range (quantidade)]    


# Inicio do programa
limpa_tela()
decoracao()


inicio = int (input ("Informe o primeiro valor: "))
final = int (input ("Informe o final: "))
quantidade = int (input ("Quantos números você quer gerar? "))
numeros = gera_numeros (inicio, final, quantidade)
n1, n2 = gera_numeros(inicio, final, quantidade)

limpa_tela()
decoracao()
print("Calculadora: ")    


mais = soma (n1,n2)
menos = subtracao (n1,n2)
vezes = multiplicacao (n1,n2)
dividido = divisao (n1,n2)

print (f'Os números são: {n1} e {n2}. A soma é {mais}, a subtração é {menos}, a multiplicação é {vezes} e a divisão é {dividido}.')
decoracao()



######################################################################
# Outra maneira de resolver (mais simples)

# def numeros_aleatorios():
#     n1 = random.randint(1,100)
#     n2 = random.randint(2,50)

#     return n1, n2
# def multiplicar (a, b):
#     return a * b

# def dividir (a, b):
#     return float (a / b)

# def somar (a, b):
#     return a + b

# def diminuir (a, b):
#     return a - b