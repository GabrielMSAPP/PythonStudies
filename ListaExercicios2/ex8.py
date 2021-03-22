'''Faça um programa para calcular e exibir a quantidade de parcelas sem juros e o valor de cada parcela, conforme o valor da compra digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Valor da Compra	Número de Parcelas
Até 100,00	2
De 100,00 a 200,00	3
De 200,00 a 400,00	4
Acima de 400,00	5'''

compra = float(input('Informe o valor da compra: '))
if compra <= 100:
    print(f'voce tera que pagar: 2 * { compra / 2}')
elif compra > 100 and compra <= 200:
    print(f'voce tera que pagar: 3 * {compra / 3}')
elif compra > 200 and compra <= 400:
    print(f'voce tera que pagar:  4* {compra / 4}')
elif compra > 400:
    print(f'voce tera que pagar: 5* {compra / 5}')