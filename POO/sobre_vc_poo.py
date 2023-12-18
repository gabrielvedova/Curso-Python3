#!/usr/bin/python3

# Fazer um programa em que diga o nome, a idade e seu trabalho(em POO)
# Imprimir quantos dias faltam para a data de aniversário
import datetime


class Pessoa:
    def __init__(self, nome, idade, trabalho):
        self.nome = nome
        self.idade = idade
        self.trabalho = trabalho

    def __str__(self):
        self.dia = datetime.datetime.day
        self.mes = datetime.datetime.month
        self.ano = datetime.datetime.year

        return f'Olá {self.nome}! Você tem {self.idade} anos, certo? \
E você é {self.trabalho}.'


def main():
    nome = input('Digite seu nome: ')
    idade = int(input('Me diga sua idade: '))
    trabalho = input('Me diga sua profissão: ')
    p1 = Pessoa(nome, idade, trabalho)
    p1.dia = 5
    p1.mes = 12
    p1.ano = 2009
    print(p1)


if __name__ == '__main__':
    main()
