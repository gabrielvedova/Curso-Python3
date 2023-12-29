from bd import nova_conexão
from mysql.connector.errors import ProgrammingError


sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Júlia', 9)

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) atualizado(s).')
