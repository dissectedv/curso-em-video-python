# programa que le um angulo e mostra o valor do seno, cosseno e tangente
from math import cos, sin, tan, radians

a = float(input('Digite um angulo: '))
a_rad = radians(a)

c = cos(a_rad)
s = sin(a_rad)
t = tan(a_rad)

print(f'\033[35mCom um angulo de {a}:\nCosseno: {c:.3f}\nSeno: {s:.3f} \nTangente: {t:.3f}')

