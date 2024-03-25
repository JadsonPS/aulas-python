"""
    Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
    com 5% de desconto.
"""

precoProdut = float(input('Digite o preço do produto: '))
newPreco = precoProdut - (precoProdut * 0.05)

print(f'O novo preço do produto é {newPreco:.2f}')
