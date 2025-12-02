# descobre a idade do jovem e mostra se ele tem que se alistar, ja passou a data ou mostra quanto tempo falta
from datetime import date

a = int(input('Digite o ano do seu nascimento: '))

ano_atual = date.today().year
idade = ano_atual - a
ano_alistamento = a + 18

if idade < 18:
    print(f'Quase lá, jovem! Você vai se alistar no ano: {ano_alistamento}! Se prepare!')
elif idade == 18:
    print(f'Você tem que se alistar neste ano! Vá servir ao Exército Brasileiro!')
else:
    print(f'Recruta, você já passou do tempo! O ano em que deveria ter se alistado foi: {ano_alistamento}.')