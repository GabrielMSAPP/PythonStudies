'''Faça um programa para calcular e exibir o desconto na compra do cliente, conforme o valor da compra do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Valor da Compra	Desconto
Até 50,00	5%
De 50,00 a 100,00	8%
De 100,00 a 150,00	12%
Acima de 150,00	15%'''

compra = float(input('Informe o valor da compra: '))
if compra <= 50:
    print(f'voce tera que pagar: {compra - compra*5/100}')
elif compra > 50 and compra <= 100:
    print(f'voce tera que pagar: {compra - compra*8/100}')
elif compra > 100 and compra <= 150:
    print(f'voce tera que pagar: {compra - compra*12/100}')
elif compra > 150:
    print(f'voce tera que pagar: {compra - compra*15/100}')