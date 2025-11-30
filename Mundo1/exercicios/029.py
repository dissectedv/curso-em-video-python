# condicao simples de velocidade do carro
vc = float(input('Qual a velocidade atual do carro? '))

if vc > 80:
    print('\033[35mMULTADO! Voce excedeu o limite permitido de 80 Km/h!')
    multa = (vc - 80) * 7
    print(f'\033[35mVoce deve pagar uma multa de R${multa:.2f}!')
print('\033[35mTenha um bom dia! Dirija com segurança!')