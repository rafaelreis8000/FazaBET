from os import system
from time import sleep
from random import choice
import emoji

system('cls')

jogo = bool(True)
while jogo == True:
    
    telainicial = input(
        '{}\n      \033[33mFAZ A BET!!!!\033[0m'
        '\n\033[36msua sorte quem faz é você\033[0m'
        '\n\n[ 1 ] JOGAR'
        '\n[ 2 ] SAIR'
        '\n\n \033[35m-->\033[0m  '
        .format('='*25)
    ).strip().upper()

    if telainicial == '1':
        break

    elif telainicial == '2':
        system('cls')
        sair = input(
            '{}DESEJA SAIR?'
            '\n\n[ 1 ] SIM'
            '\n[ 2 ] NÃO'
            '\n\n -->  '
        )

        if sair == '1':
            system('cls')
            jogo == True

        elif sair == '2':
            system('cls')
            exit()