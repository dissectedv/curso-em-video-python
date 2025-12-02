# formas de pagamento
pn = float(input("Digite o valor do produto: R$ "))
print("=" * 50)
print("     Escolha sua forma de pagamento:      ")
print("=" * 50)
print("  [1] Dinheiro ou cheque (10% de desconto): ")
print("  [2] A vista no cartao (5% de desconto): ")
print("  [3] Parcelado ate 2x no cartao:")
print("  [4] Parcelado ate 3x no cartao (com juros):")
print("=" * 50)

fp = str(input(''))

if fp == '1':
    valor = pn - (pn * 10 / 100)
    print(f'Valor final: R${valor:.2f}')
elif fp == '2':
    valor = pn - (pn * 5 / 100)
    print(f'Valor final: R${valor:.2f}')
elif fp == '3':
    print(f'Valor final: R${pn:.2f} (2x de R${pn/2:.2f})')
elif fp == '4':
    juros = 20
    valor = pn + (pn * juros / 100)
    print(f'Valor final: R${valor:.2f} (3x de R${valor/3:.2f})')
else:
    print('Opcao invalida. Tente novamente.')