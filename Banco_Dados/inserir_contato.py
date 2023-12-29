from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Lucas', '98819-1985')

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        # Commit confirma a transição para salvar no Banco de dados
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registro incluido ID:', cursor.lastrowid)

