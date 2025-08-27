# SORTEIO DA MEGA DA SENA
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import random  # importa o módulo random para gerar números aleatórios

numeros = random.sample(range(1, 61), 6)  # sorteia 6 números únicos entre 1 e 60
numeros.sort()  # ordena os números sorteados
print("Números sorteados da Mega Sena:", numeros)  # exibe os números sorteados 