def jogar():
    # importação de módulos
    from random import randint

    # cabeçalho do jogo
    print('*' * 40)
    print(f'{"Bem vindo ao jogo da adivinhação!":^40}')
    print('*' * 40)

    # escolha do número secreta
    numero_secreto = randint(1, 100)
    pontuacao = 100

    # escolha da dificuldade do jogo
    print('Qual o nível de dificuldade?')
    print('(1) Fácil | (2) Médio | (3) Difícil')
    dificuldade = int(input('Qual o nível? '))
    while dificuldade < 1 or dificuldade > 3:
        chute = int(input('Inválido. Escolha entre 1 e 100: '))

    # definição da dificuldade do jogo
    if dificuldade == 1:
        tentativas = 20
    elif dificuldade == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Digite um número entre 1 e 100: '))
        while chute > 100 or chute < 1:
            chute = int(input('Inválido. Escolha entre 1 e 100: '))

        certo = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if certo:
            print('Você acertou!')
            print(f'Sua pontuação foi {pontuacao}')
            break
        else:
            if maior:
                print('Você errou! Seu chute foi MAIOR que o número')
            elif menor:
                print('Você errou! Seu chute foi MENOR que o número')
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos
        print('-' * 33)


if __name__ == '__main__':
    jogar()
