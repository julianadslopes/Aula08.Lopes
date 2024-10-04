import os
os.system ("cls")

# Criar um programa que ajude um pescador a controlar sua produtividade.

def calculo_multa (peso_pescado):
    peso_excedente = peso_pescado - MAXIMO
    multa = peso_excedente * TAXA
    return multa, peso_excedente

# Início do programa
print ("Cálculo produtividade")

MAXIMO = 100
TAXA = 4

peso_pescado = float(input("Informe o peso pescado: "))
multa, peso_excedente = calculo_multa (peso_pescado)


if peso_pescado > 100:
    calculo_multa (peso_pescado)
    print (f'Você ultrapassou {peso_excedente}kg. Por isso, pagará R$ {multa:.2f} de multa.')
else:
    print ("Você não precisa pagar nada.")