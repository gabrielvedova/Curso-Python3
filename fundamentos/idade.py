def faixa_etaria(idade):
    if 0 <= idade < 13:
        return 'criança.'
    elif idade in range(13, 18):
        return 'adolescente.'
    elif idade in range(18, 60):
        return 'adulto.'
    elif idade >= 60:
        return 'idoso.'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    for idade in (17, 43, 100, 18, 59, -2, 0, 5):
        print(idade, ':', faixa_etaria(idade))
