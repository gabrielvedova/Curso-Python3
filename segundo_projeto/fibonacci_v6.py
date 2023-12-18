#!/usr/bin/python3

def Fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Usando o Len, vai listar os 25 primeiros números da sequência
    for fib in Fibonacci(25):
        print(fib)
