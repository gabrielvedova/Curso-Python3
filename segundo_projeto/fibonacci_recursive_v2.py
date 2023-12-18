#!/usr/bin/python3

def Fibonacci(quantidade, sequencia=(0, 1)):
    # Condição de parada
    return sequencia if len(sequencia) == quantidade else \
        Fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Imprimi os primeiros 20 números da sequência
    for fib in Fibonacci(20):
        print(fib)
