# calcula o preco da passagem conforme os kilometros
d = float(input('Qual eh a distancia da sua viagem? '))

if d <= 200:
    p1 = d * 0.50
    print(f'\033[35mVoce esta prestes a iniciar uma viagem de {d}Km!')
    print(f'E o preco da sua viagem sera {p1:.2f}')
else:
    p2 = d * 0.45
    print(f'\033[35mVoce esta prestes a iniciar uma viagem de {d}Km! (Voce paga menos!)')
    print(f'E o preco da sua viagem sera {p2:.2f}')