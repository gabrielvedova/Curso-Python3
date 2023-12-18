#!/usr/bin/python3

class Animal:
    @property
    def capacidades(self):
        return ('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('falar', 'amar', 'estudar')


class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + \
            ('bater em bandidos', 'atirar teias entre prédios')


if __name__ == '__main__':
    john = Homem()
    print(f'John: {john.capacidades}')

    dona_aranha = Aranha()
    print(f'Dona Aranha: {dona_aranha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')
