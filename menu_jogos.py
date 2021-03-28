import jogo_adivinhacao
import jogo_forca
from time import sleep


def escolhe_jogo():
    print('*' * 40)
    print(f'{"Escolha seu Jogo!":^40}')
    print('*' * 40)

    print('(1) - Forca | (2) - Adivinhação')
    jogo = int(input('Qual sua opção? '))

    if jogo == 1:
        print('Abrindo Jogo de Forca')
        sleep(1)
        jogo_forca.jogar()
    elif jogo == 2:
        print('Abrindo Jogo de Adivinhação')
        sleep(1)
        jogo_adivinhacao.jogar()

    print('FIM')


if __name__ == '__main__':
    escolhe_jogo()
