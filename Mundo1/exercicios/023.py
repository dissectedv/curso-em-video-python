# separando pela tabela de unidade dezena centena e milhar
num = int(input('Digite um numero de 0 a 9999: '))
print(f'\033[35mAnalisando o numero {num}')

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'\033[35mUnidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')