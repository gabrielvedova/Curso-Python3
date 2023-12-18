#!/usr/bin/python3
import math
import sys

ERRO = '\033[91m'
NORMAL = '\033[0m'


def help():
    print("É necessário informar o raio do círculo.")
    print("Sintaxe: {} <raio>".format(sys.argv[0]))


def circulo(raio):
    return math.pi * float(raio) ** 2


if len(sys.argv) < 2:
    help()

elif not sys.argv[1].isnumeric():
    help()
    print(ERRO, 'O raio deve ser um valor numérico!', NORMAL)
else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo:', area)
