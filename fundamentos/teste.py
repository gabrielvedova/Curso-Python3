from decimal import Decimal, getcontext

getcontext().prec = 4
print(Decimal(1) / Decimal(7))

print('O bebê\nGosto mais de você\nDo que de mim')


nome_dicionario = {'nome': ['João', 'Mario' 'Ana'],
                   'Idade': [13, 14, 17]}
nome_extra = input('Digite o seu nome: ')
nome_lista = ['João', 'Mário', 'Ana', nome_extra]

if nome_extra == 'Gabriel':
    nome_lista.remove('Mário')
    print(nome_lista)

pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': [
    'Inglês', 'Português']}
print(pessoa['nome'])
