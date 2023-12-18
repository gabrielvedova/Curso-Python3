#!/usr/bin/python3

class Data:
    def to_str(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 5
d1.mes = 4
d1.ano = 2016

print(d1.to_str())

d2 = Data()
d2.dia = 5
d2.mes = 3
d2.ano = 2009
print(d2.to_str())
