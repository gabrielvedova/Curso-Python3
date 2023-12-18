#!/usr/bin/python3

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neandertalenses'
        return self


if __name__ == '__main__':
    Jose = Humano('José')
    Gonk = Humano('Gonk').das_cavernas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'Jose.especie: {Jose.especie}')
    print(f'gonk.especie: {Gonk.especie}')
