from random import choice


def imprime_cabecalho():
    """
    Função para imprimir o título do jogo
    :return: sem retorno
    """
    print('*' * 40)
    print(f'{"Bem vindo ao jogo da forca!":^40}')
    print('*' * 40)


def escolhe_palavra():
    """
    Lê txt com as palavras e escolhe com RANDOM a palavra secreta
    :return: palavra escolhida pelo método do random
    """
    lista_paises = []
    with open('palavras.txt', 'r') as palavras:
        for linha in palavras:
            linha = linha.strip()
            lista_paises.append(linha)
    palavra_secreta = choice(lista_paises).upper()
    return palavra_secreta


def imprime_display(palavra_secreta):
    display_secreta = ['_' for _ in palavra_secreta]
    for espaco in display_secreta:
        print(espaco, end=' ')
    print()
    return display_secreta


def checagem_chute(chute, palavra, display):
    for pos, letra in enumerate(palavra):
        if chute == letra:
            display.insert(pos, chute)
            display.pop(pos + 1)
    for match in display:
        print(match, end=' ')
    print()
    return display


def imprime_forca(chances):
    if chances == 5:
        print(' ----,       ')
        print('|   (_)      ')
        print('|            ')
        print('|            ')
        print(' _______     ')
        print('|/      |    ')
    elif chances == 4:
        print(' ----,       ')
        print('|   (_)      ')
        print('|    |       ')
        print('|            ')
        print(' _______     ')
        print('|/      |    ')
    elif chances == 3:
        print(' ----,       ')
        print('|   (_)      ')
        print('|   -|       ')
        print('|            ')
        print(' _______     ')
        print('|/      |    ')
    elif chances == 2:
        print(' ----,       ')
        print('|   (_)      ')
        print('|   -|-      ')
        print('|            ')
        print(' _______     ')
        print('|/      |    ')
    elif chances == 1:
        print(' ----,       ')
        print('|   (_)      ')
        print('|   -|-      ')
        print('|   /        ')
        print(' _______     ')
        print('|/      |    ')
    elif chances == 0:
        print(' ----,       ')
        print('|   (_)      ')
        print('|   -|-      ')
        print('|   / l      ')
        print(' _______     ')
        print('|/      |    ')


def jogar():
    imprime_cabecalho()
    palavra_secreta = escolhe_palavra()
    display_secreta = imprime_display(palavra_secreta)

    # variáveis para entrar no looping
    enforca = False
    acertou = False
    chances = 6

    # looping do jogo
    while not acertou and not enforca:
        chute = str(input('Chute uma letra: ')).upper().strip()
        checagem_chute(chute, palavra_secreta, display_secreta)
        palavra_usuario = ''.join(display_secreta)
        if palavra_usuario == palavra_secreta:
            print('GANHOU!')
            acertou = True
        elif chute not in palavra_secreta:
            chances -= 1
            print(f'Não tem {chute} nesta palavra! Tentativas restantes: {chances}')
            imprime_forca(chances)
            if chances == 0:
                print('PERDEU!')
                print(f'A palavra era {palavra_secreta}')
                enforca = True
        else:
            print('jogando...')


if __name__ == '__main__':
    jogar()
