"""
12. Faça um algoritmo que leia uma temperatura em graus Celsius e apresente-a 
convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, 
na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius; 
"""

celsius = float(input('Temperatura em Celsius: '))
F = (9 * celsius + 160) / 5

print(f'{celsius}Cº = {F} Fº')
