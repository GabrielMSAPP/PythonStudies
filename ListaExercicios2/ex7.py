'''Faça um programa para calcular e exibir a valor dos juros de um empréstimo bancário, conforme o valor emprestado e o número de parcelas digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Números de Parcelas	Juros
Até 3	6%
De 3 a 6	9%
De 6 a 12	22%
Acima de 12	34%'''

valor = float(input('Informe o valor do emprestimo: '))
parcelas = int(input('Informe o valor das parcelas: '))
if parcelas <= 3:
    print(f'juros de: {parcelas * 6/100}')
elif parcelas > 3 and parcelas <= 6:
    print(f'juros de: {parcelas * 9/100}')
elif parcelas > 6 and parcelas <= 12:
    print(f'juros de: {parcelas * 22/100}')
elif parcelas > 12:
    print(f' juros de: {parcelas * 34/100}')