from bd import nova_conexão

# ASC --> Ascendente
# DESC --> Descendente


sql = 'SELECT nome FROM contatos ORDER BY nome ASC'


with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    print('\n'.join(registro[0] for registro in cursor))
