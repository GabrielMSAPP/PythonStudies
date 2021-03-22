'''Faça um programa para calcular e exibir o desconto na compra do cliente em uma farmácia, conforme o valor da compra do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Valor da Compra	Desconto Medicamento
Até 150,00	5%
De 150,00 a 300,00	7%
De 300,00 a 500,00	10%
Acima de 500,00	20%'''

compra = float(input('Informe o valor da compra: '))
if compra <= 150:
    print(f'com desconto: {compra - compra*5/100}')
elif compra > 150 and compra <= 300:
    print(f'com desconto: {compra - compra*7/100}')
elif compra > 300 and compra <= 500:
    print(f'com desconto: {compra - compra*10/100}')
elif compra > 500:
    print(f'com desconto: {compra - compra*20 /100}')