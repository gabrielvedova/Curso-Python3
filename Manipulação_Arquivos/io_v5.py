#!/usr/bin/python3

# Melhor essa versão do que a primeira,
# pois em vez de ler todo o arquivo, ele lê em pouco em pouco
with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        # sprit serve para tirar algo entre as laterais de uma string
        print('Nome: {} Idade: {}'.format(*registro.strip().split(',')))


if arquivo.closed:
    print("O arquivo foi fechado!")
