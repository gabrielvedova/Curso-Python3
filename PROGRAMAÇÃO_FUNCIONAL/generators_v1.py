#!/usr/bin/python3
def cores_arco_iris():
    yield 'vermelho'
    yield 'azul'
    yield 'amarelo'
    yield 'laranja'
    yield 'verde'
    yield 'índigo'
    yield 'violeta'


if __name__ == '__main__':
    generator = cores_arco_iris()
    print(type(generator))
    while True:
        print(next(generator))
