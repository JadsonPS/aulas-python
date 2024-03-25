"""
    Faça um programa que leia a largura e a alturade uma parede em metros,
    calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
    que cada litro de tinta, pinta uma área de 2m²
"""

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura #Calculo da área da parede

quantiTinta = area / 2 #Calculo do litro de tinta


print(f'A área é de {area}m² e é necessário {quantiTinta}L de tinta.')
