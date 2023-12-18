#!/usr/bin/python3

pessoas = [
    {'nome': 'João', 'idade': 7},
    {'nome': 'Joaquina', 'idade': 16},
    {'nome': 'Carlos', 'idade': 13},
    {'nome': 'Cleython', 'idade': 18},
    {'nome': 'Tulio', 'idade': 21},
    {'nome': 'Gabriela', 'idade': 28},
    {'nome': 'Mário', 'idade': 13},
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
nomes = filter(lambda n: len(n['nome']) > 6, pessoas)

print(list(menores))
print(list(nomes))
