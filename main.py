from os import system
from time import sleep
from random import choice
from emoji import emojize

system('cls')
saldo = float(20) #inicializa um saldo de 20 reais

while True:
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
        break

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
            print('{}\n        Saindo...'.format('='*25))
            sleep(2)
            exit()

        elif sair == '2': #Cancela a saída, o jogo volta a ser verdadeiro
            system('cls')
            sleep(0.2)
            continue

        else:
            system('cls') #erros de digitação
            sleep(0.2)
            print('{}\n \033[31mInsira um valor válido\n   e tente novamente!\033[0m'.format('='*25))
            sleep(2)






while True: #aqui inicia-se a parte do jogo verdadeiramente

    menu_inicial = bool(True)
    while menu_inicial == True:
        system('cls')
        sleep(0.2)
        
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
                    '\n\n\033[31mapostas mínimas de 1 real\033[0m'
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
                '\n  [ 5 ] Dragãozinho {}'
                '\n  [ 6 ] SAIR\033[0m'
                '\n\n   \033[35m-->\033[0m  '
                .format('='*25 , emojize(':tiger_face:') , emojize(':cow_face:') , emojize(':rabbit_face:') , emojize(':panda:') , emojize(':dragon_face:'))
            )

            if bichinho_aposta == '1':
                bichinho_aposta = 'TIGRINHO'
            elif bichinho_aposta == '2':
                bichinho_aposta = 'TOURINHO'
            elif bichinho_aposta == '3':
                bichinho_aposta = 'COELHINHO'
            elif bichinho_aposta == '4':
                bichinho_aposta = 'PANDINHA'
            elif bichinho_aposta == '5':
                bichinho_aposta = 'DRAGÃOZINHO'

            elif bichinho_aposta == '6':
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
                            print('{}\n        Saindo...'.format('='*25))
                            sleep(2)
                            exit()

                        elif sair == '2': #Cancela a saída, o jogo volta a ser verdadeiro
                            system('cls')
                            sleep(0.2)
                            continue

                        else:
                            system('cls') #erros de digitação
                            sleep(0.2)
                            print('{}\n \033[31mInsira um valor válido\n   e tente novamente!\033[0m'.format('='*25))
                            sleep(2)


            jogada = ['TIGRINHO','TOURINHO','COELHINHO','PANDINHA','DRAGÃOZINHO']
            pc = choice(jogada)

            for i in range (8): #Animação dos nomes correndo na tela, simulando "sorteio"
                for value in jogada:
                    print('{}\n\n       \033[36m{}\033[0m'.format('='*25, value))
                    sleep(0.06)
                    system('cls')

            print('{}\n\n    \033[36mE EU ESCOLHI....\033[0m \n\n      \033[35m{}!!!\033[0m'.format('='*25,pc))
            sleep(2)

            if bichinho_aposta == pc: #todas as apostas retornam o valor investido + uma porcentagem desse valor
                system('cls')
                print('{}\n\n     \033[32mVOCÊ GANHOU!!!\033[0m'.format('='*25))
                sleep(2)
                system('cls')

                if bichinho_aposta == 'TIGRINHO': #tigrinho é o que mais paga, retorna 100% do valor
                    print('{}\n\n   SEU SALDO AGORA É:\n    R${}'.format('='*25, (saldo + valor_aposta) + (saldo + valor_aposta)))
                    sleep(3)
                    break

                if bichinho_aposta == 'TOURINHO': #tourinho retorna 50%
                    print('{}\n\n   SEU SALDO AGORA É:\n    R${}'.format('='*25, (saldo + valor_aposta) + ((50/100)*valor_aposta)))
                    sleep(3)
                    break

                if bichinho_aposta == 'COELHINHO': # coelhinho retorna 25%
                    print('{}\n\n   SEU SALDO AGORA É:\n    R${}'.format('='*25, (saldo + valor_aposta) + ((25/100)*valor_aposta)))
                    sleep(3)
                    break

                if bichinho_aposta == 'PANDINHA': # pandinha retorna 15%
                    print('{}\n\n   SEU SALDO AGORA É:\n    R${}'.format('='*25, (saldo + valor_aposta) + ((15/100)*valor_aposta)))
                    sleep(3)
                    break

                if bichinho_aposta == 'DRAGÃOZINHO': # pandinha retorna 10%
                    print('{}\n\n   SEU SALDO AGORA É:\n    R${}'.format('='*25, (saldo + valor_aposta) + ((15/100)*valor_aposta)))
                    sleep(3)
                    break

            else:
                system('cls')
                print('{}\n\n     \033[31mVOCÊ PERDEU!!!\033[00m'.format('='*25))
                sleep(2)
                system('cls')

                if saldo <= 1:

                    print('{}\n\n    \033[31mSALDO INSUFICIENTE\n       VOLTE DEPOIS\033[0m'.format('='*25))
                    sleep(2)
                    exit()

                else:
                
                    nova_aposta = input(
                        '{}\nTENTAR DE NOVO?'
                        '\n\n[ 1 ] SIM'
                        '\n[ 2 ] NÃO'
                        '\n\n -->  '
                        .format('='*25)
                    )

                if nova_aposta == '1': #volta para a tela de saldo
                    break

                elif nova_aposta == '2': #encerra o programa
                    system('cls')
                    sleep(0.2)
                    print('{}\n        Saindo...'.format('='*25))
                    sleep(2)
                    exit()