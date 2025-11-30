# calcula aumento de salario
s = float(input('Qual eh o salario do funcionario? R$ '))

if s >= 1250:
    aumento = s * 0.10
    salario_total = s + aumento
    print(f'\033[35mQuem ganhava R$ {s:.2f} passa a ganhar R$ {salario_total:.2f}')
else:
    aumento = s * 0.15
    salario_total = s + aumento
    print(f'\033[35mQuem ganhava R$ {s:.2f} passa a ganhar R$ {salario_total:.2f}')