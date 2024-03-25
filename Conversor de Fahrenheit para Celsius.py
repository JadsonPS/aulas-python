"""
13. Faça um algoritmo que leia uma temperatura em Fahrenheit e a apresente 
convertida em graus Celsius. A fórmula de conversão é C = (F – 32) * ( 5 / 9), na 
qual F é a temperatura em Fahrenheit e C é a temperatura em Celcius
"""

F = float(input('Temperatura em Fº: '))
C = (F - 32) * (5 / 9)
print(f'{F}Fº = {C}Cº')
