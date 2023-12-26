from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='011219',
    database='agenda',
    auth_plugin='mysql_native_password',
)


@contextmanager
def nova_conexão():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
