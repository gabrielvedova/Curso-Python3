from bd import nova_conexão

with nova_conexão() as conexao:
    if conexao.is_connected():
        print('Conectado')
