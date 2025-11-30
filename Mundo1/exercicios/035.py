# verifica se 3 retas formam um triangulo
from time import sleep

print("\033[35m-=-"*15)
print('Analisador de Triangulo')
print('-=-'*15)

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
print('\033[35mPROCESSANDO...')
sleep(1)

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[35mForma um triângulo')
else:
    print('\033[35mNão forma um triângulo')