# calculadora de imc
p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))

imc = p / (a * a)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal ')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 35:
    print('Obesidade Grau I')
elif 35 <= imc < 40:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III (mórbida)')