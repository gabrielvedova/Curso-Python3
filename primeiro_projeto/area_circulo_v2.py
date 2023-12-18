import math
import decimal
raio = input('Informe o raio: ')
decimal.getcontext().prec = 2
area = math.pi * float(raio) ** 2
print(area)
