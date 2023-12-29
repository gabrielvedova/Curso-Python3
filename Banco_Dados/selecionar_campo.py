from bd import nova_conexão

sql = 'SELECT tel, nome FROM contatos'

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    for cont in cursor.fetchall():
        print('\t'.join(str(campo) for campo in cont))
