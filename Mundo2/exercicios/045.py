# jokenpo
from random import choice
from time import sleep

print("          JOKENPO!!!       ")

print("=" * 30)
print("Suas opções:")
print("  [0] Tesoura ")
print("  [1] Papel ")
print("  [2] Pedra")
print("=" * 30)

jogada_j = ['Tesoura', 'Papel', 'Pedra']
jogada_pc = choice(jogada_j)

escolha_str = str(input('Digite o NÚMERO da sua jogada: ')).strip()

if escolha_str == '0' or escolha_str == '1' or escolha_str == '2':
    escolha_num = int(escolha_str)
    jogador = jogada_j[escolha_num]

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=-'*12)
    print(f'Computador jogou: {jogada_pc}')
    print(f'Jogador jogou: {jogador}')
    print('-=-'*12)

    if jogador == jogada_pc:
        print('EMPATE')
    elif (jogador == 'Pedra' and jogada_pc == 'Tesoura') or \
         (jogador == 'Papel' and jogada_pc == 'Pedra') or \
         (jogador == 'Tesoura' and jogada_pc == 'Papel'):
        print('JOGADOR VENCE')
    else:
        print('COMPUTADOR VENCE')

else:
    print("Jogada inválida! Você deve digitar apenas 0, 1 ou 2.")