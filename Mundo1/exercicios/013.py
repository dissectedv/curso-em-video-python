# simula um aumento de 15% no salario
salario = float(input('Digite seu salario: '))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f'\033[35mNovo salario: {novo_salario:.2f}')