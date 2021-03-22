'''Faça um programa que receba o valor do salário mínimo, e a quantidade de quilowatts gasta por um consumidor e o tipo de consumidor (1-residencial, 2-comercial, 3-industrial) e que calcule e mostre:¶
O valor de cada quilowatt, sabendo que o quilowatt custa um oitavo do salário mínimo.
O valor a ser pago por consumidor (conta final mais o acréscimo).
O faturamento geral da empresa,
A quantidade de consumidores que pagam entre 500,00 e 1000,00.
Terminar a entrada de dados ao digitar uma quantidade de quilowatt igual a zero.
O acréscimo encontra-se na tabela a seguir:
TIPO	Percentual de acréscimo sobre o valor gasto
1	5%
2	10%
3	15%'''

faturamento = 0
valorWatt = 0
valorTotal = 0
quantCons = 0
while True:
    salario = float(input('Digite o salário mínimo: '))
    watts = float(input('Digite a quantidade de quilowatts gasto: '))
    if watts == 0:
        break
    consumidor = int(
        input('Seu tipo de consumidor (1-residencial, 2-comercial, 3-industrial)\n'))
    valorWatt = salario / 8
    valorWatts = watts * valorWatt
    if consumidor == 1:
        valorTotal = valorWatts + (valorWatts * 0.05)
    elif consumidor == 2:
        valorTotal = valorWatts + (valorWatts * 0.1)
    elif consumidor == 3:
        valorTotal = valorWatts + (valorWatts * 0.15)
    faturamento = faturamento + valorTotal
    if 500 <= valorTotal <= 1000:
        quantCons = quantCons + 1
print(f'Valor de cada QuiloWatt: {valorWatt}')
print(f'Valor pago do consumidor: {valorTotal}')
print(f'Faturamento Total da empresa: {faturamento}')
print(
    f'Quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00: {quantCons}')