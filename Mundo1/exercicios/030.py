# verifica se eh par ou impar
n = int(input('Digite um numero qualquer: '))

p = n % 2

if p == 0:
    print(f'\033[35mO numero {n} eh PAR!')
else:
    print(f'\033[35mO numero {n} eh IMPAR!')