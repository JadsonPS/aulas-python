"""
    Desenvolva um programa que leia as duas notas de um aluno,
    calcule e mostre sua média.
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))

media = (nota1 + nota2) / 2
print(f'A média do aluno foi {media:.1f}')
