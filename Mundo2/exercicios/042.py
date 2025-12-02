# verifica se 3 retas formam um triangulo, ve se eh isoceles se escaleno ou equilatero
from time import sleep

print("\033[35m-=-"*15)
print('Analisador de Triangulo')
print('-=-'*15)

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
print('\033[35mTRINGULANDO...')
sleep(1)

t = r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2

if t:
    if r1 != r2 and r3 != r1 and r2 != r3:
        print('O triangulo eh: Escaleno!')
    elif r1 == r2 == r3:
        print('O triangulo eh: Equilátero')
    else:
        print('O triangulo eh: Isósceles')
else:
    print('Os segmentos não podem formar um triângulo.')