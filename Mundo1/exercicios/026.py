# verifica quantas vezes a letra a aparece, a primeira e a ultima vez tambem
f = str(input('Digite uma frase: ')).strip().upper()

a = f.count('A')
p = f.find('A') +1
u = f.rfind('A') +1

print(f'\033[35mA letra A aparece {a} vezes\nPrimeira vez = {p}\nUltima vez = {u}')