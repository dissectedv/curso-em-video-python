# prgorama que le um numero real e mostra na tela sua parte inteira
from math import trunc

n = float(input('Digite um numero real: '))

parte_inteira = trunc(n)

print(f'\033[35mA parte inteira eh: {parte_inteira}')