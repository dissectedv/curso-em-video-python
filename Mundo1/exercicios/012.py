# algoritmo que le um produto e aplica um desconto de 5% nele
produto = float(input('Digite o valor do produto: R$ '))

desconto = produto * 0.05
preco = produto - desconto

print(f'\033[35mDesconto: {desconto}')
print(f'Preco do produto: {preco}')