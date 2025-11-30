# jogo da adivinhacao
from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar...')
print('-=-'*20)

t = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(1)

n = randint(0, 5)

if t == n:
    print(f'\033[35mEu pensei no {n} mesmo! PARABENS!')
else:
    print(f'\033[35mVoce errou! O numero era {n} e nao {t}!')