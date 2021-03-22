'''Faça um programa para calcular e exibir o desconto de IR conforme o valor do salário digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Faixa Salarial	Desconto de IR
Até 1.250,00	isento
De 1.250,00 a 1.900,00	11%
De 1.900,00 a 2.700,00	25%
Acima de 2.700,00	27.5%'''

salario = float(input('Informe seu salario:'))
if salario <= 1250:
    print('isento de IR.')
elif salario > 1250 and salario <= 1900:
    print(f'Seu salario com desconto é: {salario - salario*11/100} ')
elif salario > 1900 and salario <= 2700:
    print(f'Seu salario com desconto é: {salario - salario*25/100} ')
elif salario > 2700:
    print(f'Seu salario com desconto é: {salario - salario*27.5/100} ')