"""
94. Dado o conjunto de instruções a seguir, faça um algoritmo com quatro variações, 
colocando o comando de repetição adequadamente, de forma a: 
a) Executar o conjunto 10 vezes; 
b) Não executar nenhuma vez; 
c) Executar o conjunto 100 vezes utilizando duas estruturas de repetição; 
d) Executar N vezes, onde N é uma variável informada pelo usuário. 
- Ler A, B 
- Modulo = A mod B (calcula o resto da divisão)
"""



print("====================================")
print("Digite uma opção ")
print("[1] = 10 vezes")
print("[2] = 0 vezes")
print("[3] = 100 vezes")
print("[4] = N vezes")
opcao = int(input('Opção: '))
print("====================================")
repeticao = 0

match opcao:
    case 1:
        repeticao = 10
    case 2:
        repeticao = 0
    case 3:
        repeticao = 100
    case 4:
        repeticao = int(input('Defina a quantidade de repetição: '))
    case _:
        print('Valor invalido')

print(repeticao)

for i in range(repeticao):
    valorA = int(input('Valor A: '))
    valorB = int(input('Valor B: '))
    modulo = valorA % valorB
    print(f'O modulo entre {valorA} e {valorB} é igual a {modulo}') 