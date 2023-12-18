#!/usr/bin/python3

lista1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista1)
print(list(dobro))


lista2 = [
    {'nome': 'João', 'idade': 20},
    {'nome': 'Mário', 'idade': 27},
    {'nome': 'Gabriela', 'idade': 23}
]
so_nomes = map(lambda p: p['nome'], lista2)
print(list(so_nomes))

so_idades = map(lambda p: p['idade'], lista2)
print(list(so_idades))
print(sum(so_idades))

frases = map(lambda p: f'{p["nome"]} tem {p["idade"]} anos.', lista2)
print(list(frases))
