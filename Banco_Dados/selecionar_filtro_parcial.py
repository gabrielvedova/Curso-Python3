from bd import nova_conexão

# %letra_qualquer --> Qualquer letra que está no final de uma palavra
# %letra_qualquer% --> Qualquer letra que está no meio de uma palavra
# letra_qualquer% --> Qualquer letra que está no início de uma palavra

sql = "SELECT * FROM contatos WHERE nome like '%ca%'"

with nova_conexão() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
