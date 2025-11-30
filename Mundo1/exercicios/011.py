# calcula a area de uma parede e exibe a quantidade de tinta necessaria por metro quadrado
largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

area = largura * altura
tinta = area / 2

print(f'\033[35mSua parede tem a dimensao de {largura}x{altura} e sua area eh de: {area:.3f}m2')
print(f'Para pintar essa parede a quantidade de tinta necessaria eh de: {tinta:.4f}l de tinta')