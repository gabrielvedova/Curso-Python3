#!/usr/bin/python3
def Fibonacci(sequencia=[0, 1]):
    # Uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


if __name__ == '__main__':
    inicio = Fibonacci()
    print(inicio, id(inicio))
    print(Fibonacci(inicio))
    restart = Fibonacci()
    print(restart, id(restart))
