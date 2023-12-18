#!/usr/bin/python3

def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':

    # assert serve para ver se a expressão é verdadeira
    # assert serve mais para testar se o programa está funcionando
    # assert não retorna nada na saída se está funcionando
    assert tag_bloco('Incluído com sucesso!') == \
        '<div class="success">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!', 'error') == \
        '<div class="error">Impossível excluir!</div>'
