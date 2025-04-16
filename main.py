from os import system
from time import sleep
from random import choice
from emoji import emojize

system('cls')

jogo = bool(False)
while jogo == False:
    system('cls')
    
    telainicial = input(
        '{}\n      \033[33mFAZ A BET!!!!\033[0m'
        '\n\033[36msua sorte quem faz é você\033[0m'
        '\n\n[ 1 ] JOGAR'
        '\n[ 2 ] SAIR'
        '\n\n \033[35m-->\033[0m  '
        .format('='*25)
    ).strip().upper()

    if telainicial == '1': #O jogo se torna verdadeiro, possibilitando continuar com o jogo
        jogo = True

    elif telainicial == '2': #A opção de sair foi selecionada, mais uma checagem será feita
        system('cls')
        sleep(0.2)
        sair = input(
            '{}\n      \033[33mDESEJA SAIR?\033[0m'
            '\n\n[ 1 ] SIM'
            '\n[ 2 ] NÃO'
            '\n\n \033[35m-->\033[0m  '
            .format('='*25)
        ).strip().upper()

        if sair == '1': #Confirma saída
            system('cls')
            sleep(0.2)
            print('{}\n     Saindo...'.format('='*25))
            sleep(2)
            exit()

        elif sair == '2': #Cancela a saída, o jogo volta a ser verdadeiro
            system('cls')
            sleep(0.2)
            jogo == True

        else:
            system('cls') #erros de digitação
            sleep(0.2)
            print('{}\n \033[31mInsira um valor válido\n   e tente novamente!\033[0m'.format('='*25))
            sleep(2)




menu_inicial = bool(True)
while menu_inicial == True:
    system('cls')
    sleep(0.2)

    saldo = float(20) #o saldo será utilizado para realizar as apostas. Quando for menor que um real, você perde
    
    escolha_menu = input(
        '{}\n\033[33m    BET DOS BICHINHOS\033[0m'
        '\n\n[ 1 ] APOSTAR'
        '\n[ 2 ] SALDO'
        '\n\n \033[35m-->\033[0m  '
        .format('='*25)
    ).strip().upper()

    if escolha_menu == '1': #encerra o menu inicial, caminhando para a tela de apostas
        menu_inicial = False

    elif escolha_menu == '2': #exibe o saldo em conta
        
        system('cls')
        sleep(0.2)
        print('{}\n  \033[33mVocê tem um saldo de:\033[0m\n\n        \033[32mR${:.2f}\033[0m\n\n{}'.format('='*25 , saldo , '='*25))
        sleep(2)




tela_aposta1 = bool(True) #tela de escolha do valor da aposta
while tela_aposta1 == True:
    system('cls')
    sleep(0.2)

    try:
        valor_aposta = float(
            input(
                '{}\n\033[33mInforme o valor da aposta\033[0m'
                '\n\nSeu saldo é de \033[32mR${:.2f}\033[0m'
                '\n\n\033[31mapostas mínimas de 1 rea\033[0m'
                '\n\n \033[35m-->\033[0m R$'
                .format('='*25 , saldo)
            )
        )

        if valor_aposta > saldo: #se o valor exceder o saldo
            system('cls')
            sleep(0.2)
            print('{}\n \033[31mInsira um valor válido\n   e tente novamente!\033[0m'.format('='*25))
            sleep(2)
            continue #repete o laço

        elif valor_aposta < 1: #se a van for menor que 1
            system('cls')
            sleep(0.2)
            print('{}\n   \033[31mA aposta não pode\n ser menor que 1 real!\033[0m'.format('='*25))
            sleep(2)

        else: #se o valor estiver dentro de saldo, encerra a tela de apostas 1
            saldo = saldo - valor_aposta #remove o saldo para apostar
            tela_aposta1 = False
    
    except ValueError: #em caso de erro de digitação, caracteres especiais...
        system('cls')
        sleep(0.2)
        print('{}\n \033[31mInsira um valor válido\n   e tente novamente!\033[0m'.format('='*25))
        sleep(2)
        tela_aposta1 = True
        continue #repete o laço




    tela_aposta2 = bool(True) #tela de escolha do bichinho da aposta
    while tela_aposta2 == True:
        system('cls')
        sleep(0.2)

        bichinho_aposta = input(
            '{}\n  \033[36mQUAL SERÁ O BICHINHO'
            '\n       DA SORTE?\033[0m'
            '\n\n  \033[33m[ 1 ] Tigrinho {}'
            '\n  [ 2 ] Tourinho {}'
            '\n  [ 3 ] Coelhinho {}'
            '\n  [ 4 ] Pandinha {}'
            '\n  [ 5 ] Dragãozinho\033[0m {}'
            '\n\n   \033[35m-->\033[0m  '
            .format('='*25 , emojize(':tiger_face:') , emojize(':cow_face:') , emojize(':rabbit_face:') , emojize(':panda:') , emojize(':dragon_face:'))
        )