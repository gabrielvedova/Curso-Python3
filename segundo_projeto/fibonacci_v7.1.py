#!/usr/bin/python3

def Fibonacci(quantidade):
    resultado = [0, 1]
    # Usando o '_' pois diz que a variável no for não está sendo usada
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == '__main__':
    # Usando o Len, vai listar os 25 primeiros números da sequência
    for fib in Fibonacci(25):
        print(fib)
