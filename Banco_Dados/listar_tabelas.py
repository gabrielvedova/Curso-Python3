from bd import nova_conexão

listar_tabela = """SHOW TABLES"""

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(listar_tabela)

    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {1}: {table[0]} ')
