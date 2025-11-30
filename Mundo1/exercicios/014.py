# celsius convertido para fahrenheit e kelvim
c = float(input('Informe a temperatura em ℃ (Celsius): '))

f = c * (9 / 5) + 32
k = c + 273.15

print(f'\033[35mEm Fahnrenheit: {f} °F')
print(f'Em Kelvin: {k} K')