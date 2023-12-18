#!/usr/bin/python3

with open('pessoas.csv') as arquivo:
    # O 'w' significa que o documento txt está no modo escrita (write)!
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            # sprit serve para tirar algo entre as laterais de uma string
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print("O arquivo foi fechado!")

if saida.closed:
    print("O arquivo de saida foi fechado!")
