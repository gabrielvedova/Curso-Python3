#!/usr/bin/python3
def Fibonacci(sequencia=None):
    sequencia = sequencia or [0, 1]
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = Fibonacci()
    print(inicio, id(inicio))
    print(Fibonacci(inicio))
    restart = Fibonacci()
    print(restart, id(restart))
