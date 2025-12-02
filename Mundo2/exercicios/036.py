# verifica se o emprestimo excede ou nao o valor do salario mensal
from time import sleep

valor_casa = float(input('Qual o valor da casa? R$ '))
renda_mensal = float(input('Qual a sua renda mensal? R$ '))
anos_financiamento = int(input('Quantos anos de financiamento? '))

prestacao_mensal = valor_casa / (anos_financiamento * 12)
minimo = renda_mensal * 0.3

print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento}'
      f' a prestacao sera de R$ {prestacao_mensal:.2f}')
print(f'COMPARANDO...')
sleep(1)

if prestacao_mensal <= minimo:
    print(f'Empréstimo aprovado! Você terá que pagar R$ {prestacao_mensal:.2f} e o mínimo era: R$ {minimo:.2f}')
else:
    excede = prestacao_mensal - minimo
    print(f'Empréstimo reprovado! A prestação excede o limite em R$ {excede:.2f}')
