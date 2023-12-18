#!/usr/bin/python3

def Fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(f'{proximo}', end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    Fibonacci(20000)
