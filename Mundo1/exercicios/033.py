# verifica qual o menor e qual o maior
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

# Verifica o maior
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n3:
    maior = n2
else:
    maior = n3

# Verifica o menor
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n3:
    menor = n2
else:
    menor = n3

print(f'\033[35mO maior é {maior:.1f} e o menor é {menor:.1f}')