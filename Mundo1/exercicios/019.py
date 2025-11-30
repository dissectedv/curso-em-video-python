# sorteia aluno para limpar quadro
from random import choice

a1 = input('Digite o nome do primerio aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista_aluno = [a1, a2, a3, a4]
aluno_sorteado = choice(lista_aluno)

print(f'\033[35mO aluno escolhido foi {aluno_sorteado}')