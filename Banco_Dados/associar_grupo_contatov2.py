from mysql.connector.errors import ProgrammingError
from bd import nova_conexão

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos set grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Lucas': 'Casa',
    'Carlos': 'Trabalho',
    'Bia': 'Casa',
    'Ana': 'Trabalho',
    'Luis': 'Casa',
    'João': 'Casa',
    'Júlia': 'Trabalho',
    'Cláudio': 'Trabalho',
}

with nova_conexão() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados')
