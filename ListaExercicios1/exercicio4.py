'''Faça um programa que receba o salário-base de um funcionário, calcule e mostre o salário a receber, 
sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto 
de 7% sobre salário-base'''

sal = float(input('Informe seu salario: '))
print(f'vc ira receber: {(sal + sal*5/100) - (sal*7/100)}')