# estrutura condicional usando if elif e else
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = float(nota1 + nota2) / 2

if media >= 7:
    print(f'\033[35mCom a media de {media:.1f}:\nParabens! Voce passou!')
elif media >= 6:
    print(f'\033[35mCom a media de {media:.1f}:\nVoce esta de recuperacao!')
else:
    print(f'\033[35mCom a media de {media:.1f}:\nVoce reprovou! Estude mais!')