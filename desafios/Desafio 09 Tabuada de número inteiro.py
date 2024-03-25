"""
    Faça um programa que leia um número inteiro qualquer e mostre
    a sua tabuada.
"""

numero = int(input('Digite um número: '))
print(' '+'-'*14)
for i in range(11):
    print(f'| {numero} * {i:<2} = {numero * i:<3} |')
print(' '+'-'*14)
