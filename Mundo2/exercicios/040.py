# compara duas notas transforma em media e ve se foi aprovado, reprovado ou ta de recuperacao
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Reprovado! Estude mais!')
elif 5 <= media <= 6.9:
    print('Recuperacao! Falta pouco para passar!')
else:
    print('Aprovado! Parabens! Continue se esforcando!')