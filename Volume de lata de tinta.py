"""
14. Faça um algoritmo que calcule e apresente o valor do volume de uma lata de 
óleo, utilizando a fórmula VOLUME = 3,14159 * RAIO2
 * ALTURA. 
"""

RAIO = float(input('Raio: '))
ALTURA = float(input('Altura: '))
volume = 3.14159 * RAIO**2 * ALTURA
print(f'Volume da lata é {volume}')
