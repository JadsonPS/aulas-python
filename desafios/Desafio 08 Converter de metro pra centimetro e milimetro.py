"""
    Escreva um programa que leia um valor em metros e o exiba convertido
    em centimetros e milímetros.
"""

M = float(input('Digite um valor em Metros: '))

km  = M / 1000
hm  = M / 100
dam = M / 10

dm = M / 0.1
cm = M / 0.01
mm = M / 0.001


print(f'{km}km, {hm}hm, {dam}dam,', end=' ')
print(f'{M}m, {dm:.0f}dm,  {cm:.0f}cm, {mm:.0f}mm, ')
