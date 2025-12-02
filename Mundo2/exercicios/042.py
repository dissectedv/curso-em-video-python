# verifica se 3 retas formam um triangulo, ve se eh isoceles se escaleno ou equilatero
from time import sleep

print("\033[35m-=-"*15)
print('Analisador de Triangulo')
print('-=-'*15)

reta_1 = float(input('Digite o valor da primeira reta: '))
reta_2 = float(input('Digite o valor da segunda reta: '))
reta_3 = float(input('Digite o valor da terceira reta: '))
print('\033[35mTRINGULANDO...')
sleep(1)

triangulo = reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2

if triangulo:
    if reta_1 != reta_2 and reta_3 != reta_1 and reta_2 != reta_3:
        print('O triangulo eh: Escaleno!')
    elif reta_1 == reta_2 == reta_3:
        print('O triangulo eh: Equilátero')
    else:
        print('O triangulo eh: Isósceles')
else:
    print('Os segmentos não podem formar um triângulo.')