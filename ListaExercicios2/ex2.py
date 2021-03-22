'''Faça um programa para calcular e exibir a porcentagem de comissão de vendas de um vendedor, conforme o volume mensal de vendas do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Volume Mensal de Vendas	Comissão de Vendas
Até 5.000,00	2%
De 5.000,00 a 10.000,00	5%
De 10.000,00 a 15.000,00	7%
Acima de 15.000,00	9%'''

vendas = float(input('Informe o volume mensal de vendas: '))
if vendas <= 5000:
    print(f'Sua comissao em  vendas é: {vendas*2/100} ')
elif vendas > 5000 and vendas <= 1000:
    print(f'Sua comissao em  vendas é: {vendas*5/100} ')
elif vendas > 10000 and vendas <= 15000:
    print(f'Sua comissao em  vendas é: {vendas*7/100} ')
elif vendas > 15000:
    print(f'Sua comissao em  vendas é: {vendas*9/100} ')