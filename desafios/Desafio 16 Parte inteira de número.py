"""
    Crie um programa que leia um número Real qualquer 
    pelo teclado e mostra na tela a sua porção inteira.

    ex.: digite um número: 6.127
    O número 6.127 tem a parte inteira 6
"""
import math
from math import trunc
numero = float(input('Digite um número real: '))

porcao_inteira = math.trunc(numero)
porcao_inteira2 = trunc(numero)
porcao_inteira3 = int(numero)

print('O valor digitado foi {1} e a sua porção inteira é {0}'.format(porcao_inteira, numero))
print('O valor digitado foi {1} e a sua porção inteira é {0}'.format(porcao_inteira2, numero))
print('O valor digitado foi {1} e a sua porção inteira é {0}'.format(porcao_inteira3, numero))
