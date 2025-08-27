# LEIA O ANGULO E MOSTRE O SENO, COSSENO E TANGENTE DESSE ANGULO
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import math  # importa a biblioteca math para usar funções matemáticas
angulo = float(input("Digite o angulo que você deseja: "))  # lê o angulo do usuario
seno = math.sin(math.radians(angulo))  # calcula o seno do angulo
cosseno = math.cos(math.radians(angulo))  # calcula o cosseno
tangente = math.tan(math.radians(angulo))  # calcula a tangente
print("O angulo de {} tem o SENO de {:.2f}".format(angulo, seno))  # exibe o resultado do seno
print("O angulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))  # exibe o resultado do cosseno
print("O angulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))  # exibe o resultado da tangente
# radians() -> converte graus em radianos45
