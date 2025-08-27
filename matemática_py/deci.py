# LE UM NUMERO DECIMAL E MOSTRA SUA PARTE INTEIRA
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import math  # Importa o módulo math para usar funções matemáticas

# Solicita ao usuário que digite um número decimal e converte a entrada para float
num_user = float(input("Digite um número decimal: "))

# Obtém a parte inteira do número usando math.trunc
inteiro = math.trunc(num_user)

# Exibe a parte inteira do número informado
print("A parte inteira do número {} é {}".format(num_user, inteiro))