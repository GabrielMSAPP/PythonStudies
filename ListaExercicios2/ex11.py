'''Faça um programa que leia um número inteiro e diga se este é positivo, negativo ou zero'''

num = int(input('Informe um numero: '))
if num > 1:
    print('Positivo')
elif num == 0:
    print('zero')
elif num < 1:
    print('Negativo')