#!/usr/bin/python3

def Fibonacci():
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=',')
    while True:
        proximo = penultimo + ultimo
        print(f'{proximo},', end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    Fibonacci()
