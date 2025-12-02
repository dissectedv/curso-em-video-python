# jokenpo
from random import choice

j = str(input('Pedra, Papel ou Tesoura? ')).capitalize()

computador = ['Pedra', 'Papel', 'Tesoura']
jogada_pc = choice(computador)

print(f'Computador jogou: {jogada_pc}')

if j == jogada_pc:
    print('EMPATE')
elif (j == 'Pedra' and jogada_pc == 'Tesoura') or \
     (j == 'Tesoura' and jogada_pc == 'Papel') or \
     (j == 'Papel' and jogada_pc == 'Pedra'):
    print('JOGADOR VENCE')
elif (jogada_pc == 'Pedra' and j == 'Tesoura') or \
     (jogada_pc == 'Tesoura' and j == 'Papel') or \
     (jogada_pc == 'Papel' and j == 'Pedra'):
    print('COMPUTADOR VENCE')
else:
    print('Faca uma jogada valida!')