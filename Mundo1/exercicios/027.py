nc = str(input('Informe seu nome completo: ')).strip().title()

s = nc.split()
p = s[0]
u = s[-1]

print('\033[35mPrazer em te conhecer!')
print(f'Seu primeiro nome: {p}\nSeu ultimo nome: {u}')