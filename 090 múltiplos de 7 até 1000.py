"""
    90. Faça um algoritmo que imprima os múltiplos positivos de 7, inferiores a 1000. 
"""

for i in range(1000):
    numero = i+1
    if (numero%7 == 0):
        print(f'{numero} é múltiplo de 7')