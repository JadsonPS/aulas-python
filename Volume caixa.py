"""
18. Faça um algoritmo que leia os valores de COMPRIMENTO, LARGURA e 
ALTURA e apresente o valor do volume de uma caixa retangular. Utilize para o 
cálculo a fórmula VOLUME = COMPRIMENTO * LARGURA * ALTURA. 
"""
comprimento = float(input('COMPRIMENTO: '))
largura = float(input('LARGURA: '))
altura = float(input('ALTURA: '))
volume = comprimento * largura * altura

print('O volume da caixa {1:.2f}x{2:.2f}x{3:.2f} é igual a {0:.2f}'.format(volume, largura,altura,comprimento))