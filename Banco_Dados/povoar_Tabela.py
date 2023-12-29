from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('Casa',),
    ('Trabalho',),
)

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        # Executemany executa vários comandos de uma vez
        cursor.executemany(sql, args)
        # Commit confirma a transição para salvar no Banco de dados
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f' Foram incluídos {cursor.rowcount} registros!')
