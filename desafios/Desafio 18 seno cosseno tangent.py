"""
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, 
    cosseno e tangente desse ângulo.
"""
from math import cos, sin, tan, degrees, radians
angulo = float(input('Digite um ângulo: '))
anguloRad = radians(angulo)

seno = sin(anguloRad)
cosseno = cos(anguloRad)
tangente = tan(anguloRad)
print(f'Ângulo {angulo}°, \nSeno = {seno:.2f}, \nCosseno = {cosseno:.2f}, \nTangente = {tangente:.2f}')
