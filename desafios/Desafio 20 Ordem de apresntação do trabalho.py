""" 
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação
    de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
    mostre a ordem sorteada.

"""
"""
retipa ate a lista de sorteado for igual ao tamanho da lista de alunos
    o nome desse aluno já esta na lista de sorteados?
    se sim
        sorteie nomeamente
    se não
        adicione ele a lista
"""

from random import randint
lista_alunos = []
ordem_sorteada = []

# Entrada com os nomes dos alunos
for i in range(4):
    lista_alunos.append(input(f'Digite o nome do {i+1}º aluno/a: '))

# preenchem a lista de ordem com espaços vazios
for i in range(len(lista_alunos)):
    ordem_sorteada.append("")

#Processamento e cria a lista com os nomes dos alunos organizados de forma aleatoria
for i in range(len(lista_alunos)):
    repita = True
    while repita:
        aleatorio = randint(0, (len(lista_alunos)-1)) #um valor aleatorio entre 0 e o tamanho maximo da lista com os nomes de alunos
        if(ordem_sorteada[aleatorio] == ""):
            ordem_sorteada[aleatorio] = lista_alunos[i]
            repita = False

#Saída de dados mostrando a lista com a sequência de alunos
for i in range(len(ordem_sorteada)):
    print(f"{i+1}º aluno: {ordem_sorteada[i]}")





#===================================== V2 =============================================
from random import choice, shuffle

alunos = []
ordem = []
for cont in range(4):
    alunos.append(input(f"{cont + 1}º aluno: "))

print(shuffle(alunos))

