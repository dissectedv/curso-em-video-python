# verifica se existe silva no nome
nc = str(input('Digite seu nome completo: ')).strip()

v = 'SILVA' in nc.upper()

print(f'\033[35m{v}')

