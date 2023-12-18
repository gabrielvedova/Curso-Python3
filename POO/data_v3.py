#!/usr/bin/python3

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 4, 2016)
print(d1)

d2 = Data(5, 3, 2009)
print(d2)
