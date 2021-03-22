'''Faça um programa que simule uma calculadora com as quatro operações básicas (+, -, *, / ). 
O programa deve solicitar ao usuário a entrada de dois operandos e da operação a ser executada, 
na forma de menu. Dependendo da opção escolhida, deve ser executada a operação solicitada e 
escrito seu resultado. Utilize uma variável do tipo inteiro para armazenar a operação e utilize o
comando caso para escolher a operação a ser executada a partir do operador'''

num1 = float(input('Informe um valor: '))
num2 = float(input('Informe um valor: '))
op = input('Informe o operando q deseja - + * /  :')
if op == '+':
    print(num1+num2)
if op == '-':
    print(num1-num2)
if op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)