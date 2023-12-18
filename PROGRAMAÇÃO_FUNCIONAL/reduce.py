#!/usr/bin/python3

from functools import reduce

pessoas = [
    {'nome': 'João', 'idade': 7},
    {'nome': 'Joaquina', 'idade': 16},
    {'nome': 'Carlos', 'idade': 13},
    {'nome': 'Cleython', 'idade': 18},
    {'nome': 'Tulio', 'idade': 21},
    {'nome': 'Gabriela', 'idade': 28},
    {'nome': 'Mário', 'idade': 13},
]

so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)

soma_idades = reduce(lambda idades, idade: idades + idade, menores, 0)

print(soma_idades)
