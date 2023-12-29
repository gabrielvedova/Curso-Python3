from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Carlos', '96719-1985'),
    ('Bia', '98729-1985'),
    ('Ana', '98519-4385'),
    ('Luis', '98703-1235'),
    ('João', '98418-1982'),
    ('Carla', '98679-1030'),
    ('Yan', '94256-1985'),
    ('Cláudio', '98769-1990'),
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
