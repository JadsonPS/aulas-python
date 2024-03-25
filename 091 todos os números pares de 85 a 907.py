""" 
    91. Faça um algoritmo que imprima todos os números pares compreendidos entre 
85 e 907. O algoritmo deve também calcular a soma destes valores.
 """

soma = 0
for numero in range(908):
    if(numero >= 85 ) and (numero%2 == 0):
        soma += numero
else:
    print(soma)