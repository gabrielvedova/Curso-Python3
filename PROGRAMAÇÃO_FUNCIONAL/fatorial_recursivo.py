#!/usr/bin/python3

def fatorial(n):
    return (n * fatorial(n - 1) if n - 1 > 1 else 1)


if __name__ == '__main__':
    n = int(input('Me diga aí um número aleatório: '))
    print(f'{n}! = {fatorial(n)}')
