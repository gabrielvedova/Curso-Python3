PALAVRAS_PROIBIDAS = {'futebol', 'política', 'religião'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for texto in textos:
    intercecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intercecao:
        print("Texto possui duas palavras proibidas: ", intercecao)

    else:
        print("Texto autorizado: ", texto)