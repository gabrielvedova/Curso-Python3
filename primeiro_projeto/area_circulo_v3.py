import math


def circulo(raio):
    return math.pi * float(raio) ** 2


raio = input('Informe o raio: ')
area = circulo(raio)
print('Área do círculo:', area)
