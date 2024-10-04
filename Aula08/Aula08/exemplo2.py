import os
os.system ("cls")

# Biblioteca para números aleatórios
import random

# num = random.randint (1,10) # número aleatório entre 1 e 10

def gera_numeros (inicio, final, quantidade):
    return [random.randint(inicio, final) for i in range (quantidade)]    


inicio = int (input ("Informe o primeiro valor: "))
final = int (input ("Informe o final: "))
quantidade = int (input ("Quantos números você quer gerar? "))

numeros = gera_numeros (inicio, final, quantidade)

print (numeros)
