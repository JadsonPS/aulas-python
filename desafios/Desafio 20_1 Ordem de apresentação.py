""" 
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação
    de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
    mostre a ordem sorteada.

"""


from random import shuffle

alunos = []
ordem = []
for cont in range(4):
    alunos.append(input(f"{cont + 1}º aluno: "))
print(alunos)

shuffle(alunos) # Ele embaralha os valores na lista
print(alunos)
