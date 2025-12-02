# formas de pagamento
valor_produto = float(input("Digite o valor do produto: R$ "))
print("=" * 50)
print("     Escolha sua forma de pagamento:      ")
print("=" * 50)
print("  [1] Dinheiro ou cheque (10% de desconto): ")
print("  [2] A vista no cartao (5% de desconto): ")
print("  [3] Parcelado ate 2x no cartao:")
print("  [4] Parcelado ate 3x no cartao (com juros):")
print("=" * 50)

forma_pagamento = str(input(''))

if forma_pagamento == '1':
    valor = valor_produto - (valor_produto * 10 / 100)
    print(f'Valor final: R${valor:.2f}')
elif forma_pagamento == '2':
    valor = valor_produto - (valor_produto * 5 / 100)
    print(f'Valor final: R${valor:.2f}')
elif forma_pagamento == '3':
    print(f'Valor final: R${valor_produto:.2f} (2x de R${valor_produto/2:.2f})')
elif forma_pagamento == '4':
    juros = 20
    valor = valor_produto + (valor_produto * juros / 100)
    print(f'Valor final: R${valor:.2f} (3x de R${valor/3:.2f})')
else:
    print('Opcao invalida. Tente novamente.')