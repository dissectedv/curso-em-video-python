# pede um numero, mostra o dobro o triplo e a raiz quadrada dele
n = int(input('Digite um numero: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print(f'\033[35mO dobro de {n} eh: {d}\nO triplo de {n} eh: {t}\nA raiz quadrada de {n} eh: {r:.2f}')