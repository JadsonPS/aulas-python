"""
16. Faça um algoritmo que leia dois valores para as variáveis A e B e efetue a troca 
dos valores de forma que a variável A passe a possuir o valor da variável B e a 
variável B passe a possuir o valor da variável A. Apresente os valores trocados. 
"""

valorA = int(input('Digite o valor A: '))
valorB = int(input('Digite o valor B: '))
valorC = valorA
valorA = valorB
valorB = valorC

print('O valor de A = {} e o valor de B = {}'.format(valorA, valorB))