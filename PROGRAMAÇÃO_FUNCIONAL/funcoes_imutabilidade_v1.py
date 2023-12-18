#!/usr/bin/python3
from functools import reduce
from operator import add

valores = [30, 10, 25, 70, 100, 94]

# opção 1
print(sorted(valores))
print(valores)

# opção 2
valores.sort()
print(valores)

print(min(valores))
print(max(valores))

print(sum(valores))
print(reduce(add, valores))

print(reversed(valores))
print(list(reversed(valores)))
