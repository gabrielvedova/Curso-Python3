import math
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal(math.pi) * Decimal(5.2) ** 2)

raio = 5.2
area = math.pi * raio ** 2
print(area)
