#!/usr/bin/python3

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neandertalenses'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neandertalenses', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neandertal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    gonk = Neandertal('Gonk')

    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')

    print(f'Homo Sapiens é evoluído? {HomoSapiens.is_evoluido()}')
    print(f'Neandertal é evoluído? {Neandertal.is_evoluido()}')
    print(f'José evoluído? {jose.is_evoluido()}')
    print(f'Gonk evoluído? {gonk.is_evoluido()}')
