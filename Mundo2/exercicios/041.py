# verifica ano de nascimento e verifica a categoria na natacao
from datetime import date

ano_nascimento = int(input('Digite o seu ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos de idade.')

if idade <= 9:
    print('Classificacao: Mirim.')
elif idade <= 14:
    print('Classificacao: Infantil.')
elif idade <= 19:
    print('Classificacao: Junior.')
elif idade <= 25:
    print('Classificacao: Senior.')
else:
    print('Classificacao: Master.')