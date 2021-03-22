'''Faça um programa que receba o salário de um funcionário
 e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário'''

sal = float(input('Informe seu salario: '))
aum = int(input('Informe o percentual de aumento: '))
print(f'Seu aumento foi de: {sal*aum/100}')
print(f'Seu novo salario é: {sal + sal*aum/100}')