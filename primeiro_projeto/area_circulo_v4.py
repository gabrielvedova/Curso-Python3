import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


raio = sys.argv[1]
area = circulo(raio)
print('Área do círculo:', area)
