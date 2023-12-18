#!/usr/bin/python3


class Potencia:
    # Calcular uma potência específica
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3² => {quadrado(3)}')
        print(f'5² => {quadrado(5)}')
        print(f'4⁵ => {Potencia(4)(5)}')
