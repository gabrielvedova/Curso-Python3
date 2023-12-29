from bd import nova_conexão

# %letra_qualquer --> Qualquer letra que está no final de uma palavra
# %letra_qualquer% --> Qualquer letra que está no meio de uma palavra
# letra_qualquer% --> Qualquer letra que está no início de uma palavra

sql = "SELECT * FROM contatos WHERE nome like %s"

with nova_conexão() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )

    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
