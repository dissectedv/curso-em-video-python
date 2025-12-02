# verifica ano de nascimento e verifica a categoria na natacao
from datetime import date

adn = int(input('Digite o seu ano de nascimento: '))

atu = date.today().year
idade = atu - adn

if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil.')
elif idade <= 19:
    print('Junior.')
elif idade <= 20:
    print('Senior.')
else:
    print('Master')