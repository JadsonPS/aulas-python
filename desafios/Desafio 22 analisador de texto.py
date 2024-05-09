"""
    Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas
    - O nome com todas minúsculas
    - Quantas letras ao todo (sem considerar espaços).
    - Quantas letras tem o primeiro nome.
"""

nome = str(input("Digite um nome completo: "))

print("Maiúsculo = ",nome.upper())
print("Minúsculo = ",nome.lower())
print("Total de letras sem epaços = ",len(''.join(nome.split())))
primeiroNome = nome.split()
print("Total de letras o primeiro nome = ",len(primeiroNome[0]))





