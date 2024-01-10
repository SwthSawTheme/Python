import random
import time

while True:
    print('Pedra[1], Papel[2] ou Tesoura[3]??\n')

    escolha_jogador = input('Escolha: ')

    lista = ['Pedra', 'Papel', 'Tesoura']
    escolha_pc = random.choice(lista)

    print(f'O computador escolheu {escolha_pc}')

    if escolha_jogador == escolha_pc:
        print('Empate!\n')
    elif (escolha_jogador == '1' and escolha_pc == 'Tesoura') or \
         (escolha_jogador == '2' and escolha_pc == 'Pedra') or \
         (escolha_jogador == '3' and escolha_pc == 'Papel'):
        print(f'Jogador venceu!\n')
    else:
        print('O computador venceu!\n')
