'''Faça um programa para calcular e exibir o desconto de INSS conforme o valor do salário digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Faixa salarial	Desconto de INSS
Até 600,00	7%
De 600,00 a 800,00	8%
De 800,00 a 1.200,00	9%
Acima de 1.200,00	11%'''

salario = (float(input('Informe um salario:')))
if salario <= 600:
    print(f'Seu salario com desconto é: {salario - salario*7/100} ')
elif salario > 600 and salario <= 800:
    print(f'Seu salario com desconto é: {salario - salario*8/100} ')
elif salario > 800 and salario <= 1200:
    print(f'Seu salario com desconto é: {salario - salario*9/100} ')
elif salario > 1200:
    print(f'Seu salario com desconto é: {salario - salario*11/100} ')