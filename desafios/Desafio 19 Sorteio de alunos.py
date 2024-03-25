"""
    Um professor quer sortear um dos seus quatro alunos para 
    apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e
    escrevendo o nome do escolhido.
"""
import random
#lista com nomes dos alunos
nomes_alunos = []

#entrada dos nomes dos alunos
for i in range(4):
    nomes_alunos.append(str(input(f"Nome {i+1}º aluno/a: ")))

#sorteio do aluno de forma aleatoria
aluno_escolhido = nomes_alunos[random.randint(0, 3)]

print(f'O aluno sorteado foi {aluno_escolhido}!')


# usando a função choice do modulo Random podemos pegar um valor de forma aleatoria
escolhido = random.choice(nomes_alunos)
print(f'Escolhido {escolhido}')