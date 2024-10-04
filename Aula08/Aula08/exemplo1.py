import os
os.system ("cls")

# def calcula_dobro (x):
#     dobro = x * 2
#     return dobro


# # Parte principal
# num = float (input("Informe o número: "))    

# resultado = calcula_dobro (num)
# print(resultado)


########################################################

def calcula_dobro_triplo (x):
    dobro = x * 2
    triplo = x * 3
    return dobro , triplo


# Parte principal 
num = float (input("Número: "))

dobro, triplo = calcula_dobro_triplo (num)    # dobro e triplo também podem ser chamados de outra forma (como x2 e x3 por ex)

print(f'O dobro é {dobro} e o triplo é {triplo}')