'''Faça um programa que receba um número positivo e maior que zero, calcule e mostre:¶
O número digitado ao quadrado;
O número digitado ao cubo;
A raiz quadrada do número digitado;
A raiz cúbica do número digitado;
A soma do quadrado mais o cubo do número digitado.'''

import math
n = int(input('Informe um numero positivo: '))
if n > 0:
    print(f'O numero ao quadrado é: {pow(n, 2)}')
    print(f'O numero ao cubo é: {pow(n, 3)}')
    print(f'A raiz quadrada é: {math.sqrt(n)}')
    print(f'A raiz cubica é: {n ** 1/3}')
    print(f'A soma do quadrado + o cubo é: {pow(n, 2) + pow(n, 3)}')