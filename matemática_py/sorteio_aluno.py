# SORTEAR UM DOS QUATRO ALUNOS PARA APAGAR O QUADRO
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import random  # importa o módulo random para gerar números aleatórios

alunos = ['Ana', 'Bruno', 'Carlos', 'Diana']  # nomes dos alunos
escolhido = random.choice(alunos)  # sorteia um aluno

print(f'O aluno sorteado para apagar o quadro foi: {escolhido}')

