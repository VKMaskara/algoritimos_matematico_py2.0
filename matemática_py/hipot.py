# leia o comprimento dos catetos de um triangulo retangulo e mostre o comprimento da hipotenusa
# AUTOR: VITOR KAUÊ
# DATA: 24/06/2024
import math  # importa a biblioteca math para usar a função sqrt
c1 = float(input("\nDigite o comprimento do cateto oposto: "))  # lê o comprimento do cateto oposto
c2 = float(input("Digite o comprimento do cateto adjacente: "))  # lê o comprimento do cateto adjacente
h = math.hypot(c1, c2)  # calcula a hipotenusa usando a função hypot
print("O comprimento da hipotenusa é {:.2f}".format(h))  # exibe o resultado com duas casas decimais
# hypot(x, y) -> sqrt(x*x + y*y)