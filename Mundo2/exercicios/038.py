# compara dois numeros e indica se um eh maior e outro eh menor ou se os dois sao iguais
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print(f'O primeiro valor eh maior! {n1} eh maior que {n2}')
elif n1 < n2:
    print(f'O segundo valor eh maior! {n2} eh maior que {n1}')
else:
    print('Nao existe valor maior. Os dois sao iguais.')