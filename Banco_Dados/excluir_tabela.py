from bd import nova_conexão

excluir_tabela = """DROP TABLE emails"""

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(excluir_tabela)
