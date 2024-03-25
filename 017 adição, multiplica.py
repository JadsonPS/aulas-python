""" 
    17. Faça um algoritmo que leia quatro números e apresente os resultados de adição 
e multiplicação dos valores entre si, baseando-se na utilização da propriedade 
distributiva, ou seja, se forem lidas as variáveis A, B, C e D, devem ser somadas 
e multiplicadas A com B, A com C e A com D; B com C, B com D e por último C 
com D.
 """

""" 
a + b
a + c 
a + d 

b + c 
b + d

c + d 
"""
number_list = []
for i in range(0, 4, 1):
    number_list.append(int(input(f'Digite o {i+1}º número: ')))
""" print(number_list) """

""" 
a + b
a + c 
a + d 
"""
for cont in range(1, 4):
    print(f'{number_list[0]} + {number_list[cont]} = {number_list[0] + number_list[cont]}')
else:
    print('\n')
""" 
b + c 
b + d
"""
for cont in range(2, 4):
    print(f'{number_list[1]} + {number_list[cont]} = {number_list[1] + number_list[cont]}')
else:
    print('\n')
""" c + d  """
print(f'{number_list[2]} + {number_list[3]} = {number_list[2] + number_list[3]} \n')




""" 
a * b
a * c 
a * d 
"""
for cont in range(1, 4):
    print(f'{number_list[0]} * {number_list[cont]} = {number_list[0] * number_list[cont]}')
else:
    print('\n')
""" 
b * c 
b * d
"""
for cont in range(2, 4):
    print(f'{number_list[1]} * {number_list[cont]} = {number_list[1] * number_list[cont]}')
else:
    print('\n')
""" c * d  """
print(f'{number_list[2]} * {number_list[3]} = {number_list[2] * number_list[3]}')