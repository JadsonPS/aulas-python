"""
    88. Some os números de 1 a 100 e imprima o valor. 
"""
some = 0

for cont in range(100):
    #print(cont+1)
    some += (cont+1)
else:
    print(f'Fim do for a soma de todos os números entre 1 e 100 é igual a {some}')