from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='011219',
    auth_plugin='mysql_native_password',
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')


for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
