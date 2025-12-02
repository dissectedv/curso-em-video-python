# converte numero para binario octal e hexadecimal
n = int(input('Digite um numero inteiro qualquer: '))
print("=" * 40)
print("     CONVERSOR DE BASES NUMÉRICAS      ")
print("=" * 40)
print("  [1] Binário")
print("  [2] Octal")
print("  [3] Hexadecimal")
print("  [4] Mostrar todos")
print("=" * 40)
al = str(input('')).strip()

if al == '1':
    b = bin(n)[2:]
    print(f'Binario: {b}')
elif al == '2':
    o = oct(n)[2:]
    print(f'Octal: {o}')
elif al == '3':
    h = hex(n)[2:]
    print(f'Hexadecimal: {h}')
elif al == '4':
    b = bin(n)[2:]
    o = oct(n)[2:]
    h = hex(n)[2:]
    print(f"Binário: {b}, Octal: {o}, Hexadecimal: {h}")
else:
    print('Opcao Invalida! Escolha 1, 2, 3 ou 4')