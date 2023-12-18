#!/usr/bin/python3

# Melhor essa versão do que a primeira,
# pois em vez de ler todo o arquivo, ele lê em pouco em pouco
arquivo = open("pessoas.csv")
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')))

arquivo.close()
