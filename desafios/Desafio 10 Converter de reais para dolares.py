"""
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
    e mostre quantos Dólares ela pode comprar
    Considere US$1,00 = R$3,27 
"""

valorR = float(input('Quanto dinheiro você tem na carteira R$: '))
valorD = valorR*1/3.27

print(f'O valor R${valorR:.2f} é equivalente a US${valorD:.2f}')
