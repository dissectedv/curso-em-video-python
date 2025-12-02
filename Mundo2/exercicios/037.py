# converte numero para binario octal e hexadecimal
numero = int(input('Digite um numero inteiro qualquer: '))
print("=" * 40)
print("     CONVERSOR DE BASES NUMÉRICAS      ")
print("=" * 40)
print("  [1] Binário")
print("  [2] Octal")
print("  [3] Hexadecimal")
print("  [4] Mostrar todos")
print("=" * 40)
opcao = str(input('Sua opcao: ')).strip()

if opcao == '1':
    b = bin(numero)[2:]
    print(f'Binario: {b}')
elif opcao == '2':
    o = oct(numero)[2:]
    print(f'Octal: {o}')
elif opcao == '3':
    h = hex(numero)[2:]
    print(f'Hexadecimal: {h}')
elif opcao == '4':
    b = bin(numero)[2:]
    o = oct(numero)[2:]
    h = hex(numero)[2:]
    print(f"Binário: {b}, Octal: {o}, Hexadecimal: {h}")
else:
    print('Opcao Invalida! Escolha 1, 2, 3 ou 4')