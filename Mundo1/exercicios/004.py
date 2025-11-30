# pede algo, verifica o tipo e fazer verificacoes com is
a = input('digite algo: ')

print('\033[35mO tipo primitivo desse algo eh: ', type(a))
print('So tem espacos?' , a.isspace())
print('Eh numerico?' , a.isnumeric())
print('Eh alfabetico? ', a.isalpha())
print('Eh alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())