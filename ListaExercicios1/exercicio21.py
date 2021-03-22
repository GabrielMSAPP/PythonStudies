'''Escreva um programa que solicite ao usuário dois números e apresente na tela os resultados das 
operações aritméticas (soma, subtração, multiplicação, divisão, resto da divisão, exponenciação, radiciação)'''

import math
num1 = float(input('Informe um numero: '))
num2 = float(input('Informe outro numero: '))
print(f'a soma dos numeros sao: {num1+num2}')
print(f'a subtracao dos numeros sao: {num1-num2}')
print(f'a multiplicacao dos numeros sao: {num1*num2}')
print(f'a divisao dos numeros sao: {num1/num2}')
print(f'o resto da divisao dos numeros sao: {num1%num2}')
print(f'a exponenciacao dos numeros sao: {math.exp(num1), math.exp(num2)}')
print(f'a radiciacao dos numeros sao: {math.sqrt(num1), math.sqrt(num2)}')