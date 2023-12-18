#!/usr/bin/python3

def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n

    return soma


if __name__ == '__main__':

    # packing
    print(soma_2(4, 3))
    print(soma_3(4, 7, 9))
    print(soma_n(2, 4, 5, 6, 9))
    print(soma_n(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

    # unpacking
    tupla_nums = (1, 2, 3)
    print(soma_n(*tupla_nums))

    lista_nums = (1, 2, 3)
    print(soma_n(*lista_nums))
