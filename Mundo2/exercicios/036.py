# verifica se o emprestimo excede ou nao o valor do salario mensal
vc = float(input('Qual o valor da casa? '))
r = float(input('Qual a sua renda mensal? R$ '))
qa = float(input('Qual a quantidade de anos a pagar? '))

pm = vc / (qa * 12)

l = r * 0.3

if pm <= l:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo reprovado! Prestacao excede 30% do salario.')
