# programa que le nome de cidade e verifica se comeca com o nome SANTO
c = str(input('Digite o nome da cidade que nasceu: ')).strip()
print('Analisando o nome...')

v = c[:5].upper() == 'SANTO'

print(f'\033[35mO nome da cidade comeca com Santo? {v}')