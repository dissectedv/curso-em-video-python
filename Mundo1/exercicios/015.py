# pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km foram percorridos? '))

km = km * 0.15
dias = dias * 60
aluguel = km + dias

print(f'\033[35mO total a pagar eh de R$ {aluguel:.2f}')