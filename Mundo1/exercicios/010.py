# converte real em moedas estrangeiras
real = float(input('Quanto dinheiro voce tem na carteira? R$: '))

dolar = real / 5.34
euro = real / 6.19
libra = real / 7.06
yen = real / 0.034

print(f'\033[35mCom {real:.2f} voce pode comprar: \nUS$ (Dolar): {dolar:.2f}\n€ (Euro): {euro:.2f}\n£ (Libra): {libra:.2f}\n¥ (Yen): {yen:.2f}')