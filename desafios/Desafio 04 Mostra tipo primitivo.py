#desafio04

"""
    Faça um programa que leia algo pelo teclado e mostre na tela o seu
    tipo primitivo e todas as informações possítivas sobre ele.
"""

entrada = input('Digite algo: ')
print('O tipo primitivo é  ', type(entrada))
print('Só tem espaços?     ', entrada.isspace())
print('É um número?        ', entrada.isnumeric())
print('É alfabético?       ', entrada.isalpha()) # mostra que é alphanumerico
print('É alfanumérico?     ', entrada.isalnum())
print('Está em maiúsculas? ', entrada.isupper())
print('Está em minúsculas? ', entrada.islower())
print('Está capitalizada?  ', entrada.istitle())
