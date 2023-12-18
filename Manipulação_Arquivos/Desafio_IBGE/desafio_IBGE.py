#!/usr/bin/python3

from urllib import request
import csv


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV......')
        dados = entrada.read().decode('latin1')
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')


if __name__ == '__main__':
    read(r'https://files.cod3r.com.br/curso-python/desafio-ibge.csv')
