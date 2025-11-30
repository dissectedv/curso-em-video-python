# transforma metros em todos os dados da tabela de medidas de comprimento
metros = float(input('Digite um valor em metros: '))

km = metros / 1000
hm = metros / 100
dam = metros / 10
d = metros * 10
c = metros * 100
mi = metros * 1000

print(f'\033[35mKilometros: {km:.2f}\nHectometros: {hm:.2f}\nDecametros: {dam:.2f}\nDecimetros: {d:.0f}\nCentimetros: {c:.0f}\nMilimetros: {mi:.0f}')