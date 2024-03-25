"""
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
    de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

    A² = B²+C²
    A = raiz(b² + c²)
"""

from math import sqrt, hypot

catetoA = float(input('Digite o comprimento do cateto oposto: '))
catetoB = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = sqrt(catetoA**2 + catetoB**2)
H = (catetoA**2 + catetoB**2)**(1/2)
hipot = hypot(catetoA, catetoB)

print(f'O valor da hipotenusa é = {hipotenusa:.2f} ou {H} ou {hipot}')