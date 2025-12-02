# descobre a idade do jovem e mostra se ele tem que se alistar, ja passou a data ou mostra quanto tempo falta
from datetime import date

sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]
ano_nascimento = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = ano_nascimento + 18

print(f'\nQuem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if sexo == 'M':
    if idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
        print(f'Seu alistamento será em {ano_alistamento}.')
    elif idade == 18:
        print(f'Você tem que se alistar IMEDIATAMENTE!')
    else:
        saldo = idade - 18
        print(f'Seu alistamento foi em {ano_alistamento}.')

elif sexo == 'F':
    print('O alistamento militar é facultativo para mulheres.')
    escolha = str(input('Você deseja se alistar? (S/N): ')).strip().upper()[0]

    if escolha == 'S':
        if idade < 18:
            saldo = 18 - idade
            print(f'Faltam {saldo} ano(s). Seu ano de alistamento será: {ano_alistamento}.')
        elif idade == 18:
            print(f'Compareça a uma junta militar este ano!')
        else:
            print(f'O ano do seu alistamento padrão seria em {ano_alistamento}.')
    elif escolha == 'N':
        print('Tudo bem! Tenha um ótimo dia!')
    else:
        print('Opção inválida.')

else:
    print('Opção de sexo inválida.')