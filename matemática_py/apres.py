# O MESMO PROFESSOR QUESORTEAR A ORDEM DE APRESENTAÇÃO, FAÇA UM PROGRAMA QUE LE O NOME DOS 4 ALUNOS E MOSTRE A ORDEM DE CADA UM
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import random

alunos = []
for i in range(4):
    name = input(f"Digite o nome do {i+1}º aluno: ")
    alunos.append(name)
    random.shuffle(alunos)
print("A ordem de apresentação será:")
for i, aluno in enumerate(alunos, start=1): 
    print(f"{i}º - {aluno}")