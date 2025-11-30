# programa que le o nome compleo e retorna informacoes:
# (maiuscula minuscula, quantas letras ao todo sem contar espacos,
# quantas letras tem o primeiro nome)

n = str(input('Informe seu nome completo: ')).strip()
print('\033[35mAnalisando seu nome...')

se = n.replace(' ', '')
d = n.split()

print(f'\033[35mSeu nome em maiusculas eh: {n.upper()}')
print(f'Seu nome em minuscular eh: {n.lower()}')
print(f'Seu nome ao todo tem {len(se)} letras')
print(f'Seu primeiro nome eh {d[0]} e ele tem {len(d[0])} letras')
