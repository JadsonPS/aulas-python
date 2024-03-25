print(122%2)
print(27**(1/3)) #Essa é a Raiz cubica de 27 que dá 3
print(f"A raiz quadrada de 9 é {int(9**(1/2))}")

nome = input('Qual é seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multi = n1 * n2
divi = n1 / n2
diviIntei = n1 // n2
poten = n1 ** n2

print(f'A soma \n é {soma}, produto é {multi} e a divisão é {divi:.3f}', end=' ')
print(f'Divisão inteira {diviIntei} e potência {poten}')


