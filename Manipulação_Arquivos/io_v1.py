#!/usr/bin/python3

# Abre o arquivo csv e coloca em uma variável
arquivo = open('pessoas.csv')
# Lê toda a variável arquivo e coloca na variável dados
dados = arquivo.read()
# Fecha a variável arquivos
arquivo.close()


# splitlines serve para separar cada conteúdo que foi definido em cada linha
for registro in dados.splitlines():
    # split serve para separar as variáveis por algo que foi definido
    print("Olá! Meu nome é {} e eu tenho {} anos".format(*registro.split(',')))
