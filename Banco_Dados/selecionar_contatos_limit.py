from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'SELECT * FROM contatos LIMIT 5'

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for cont in contatos:
            print(f'{cont[2]:2d} -- {cont[0]:20s} Telefone: {cont[1]}')
