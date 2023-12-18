#!/usr/bin/python3

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias

mes_31 = filter(lambda mes: mdays[mes] == 31, range(1, 13))
mes_nome = map(lambda mes: month_name[mes], mes_31)
juntar_meses = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
                      mes_nome, 'Meses com 31 dias:')

print(juntar_meses)
