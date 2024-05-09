"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
com o nome "Santo".
"""

cidade = str(input('Em que cidade você nasceu? ')).split()


print(cidade[0].lower() == "santo")
