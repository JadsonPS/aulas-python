"""
92. Faça um algoritmo que calcule o valor de A, dado por: 
    A = N + (N-1)/2 + (N-2)/3 + ... + 1/N , onde N é um número inteiro positivo.
"""
numeroN = int(input('Entre com o valor de N: '))

valorA = 0
for cont in range(numeroN):
    valorA = valorA + ((numeroN - cont) / (cont + 1 ))
print(valorA)

