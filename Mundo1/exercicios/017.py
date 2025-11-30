# le o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e mostra o cumprimento da hipotenusa
from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(ca, co)

print(f'\033[35mCom um cateto oposto de {co} e um cateto adjacente de {ca} a hipotenusa tem o valor {hipotenusa:.2f}')
