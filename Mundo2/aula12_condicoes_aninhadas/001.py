# Condicoes aninhadas
n = str(input('Digite seu nome: '))

if n == 'Joao':
    print('Que nome bonito!')
elif n == 'Joaquim' or n == 'Joana':
    print('Que nome legal!')
elif n in 'Ana Claudia Paula':
    print('Que nome feminino maneiro!')
else:
    print('Que nome normal!')
print('Tenha um bom dia!')