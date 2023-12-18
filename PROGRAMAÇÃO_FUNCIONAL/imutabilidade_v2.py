#!/usr/bin/python3

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias


def mes_31(mes): return mdays[mes] == 31


def get_nome(mes): return month_name[mes]


def juntar_meses(todos, nome_mes): return f'{todos}\n- {nome_mes}'


print(reduce(juntar_meses,
             map(get_nome, filter(mes_31, range(1, 13))),
             'Mês com 31 dias: '))
