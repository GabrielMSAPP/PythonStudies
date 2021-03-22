'''Ler um número inteiro qualquer e multiplicá-lo por 2.
Apresentar o resultado da multiplicação somente se o resultado for maior que 30'''

num = int(input('Informe um numero: '))
num *= 2
if num * 2 > 30:
    print(num)
else:
    print('Numero menor que 30')