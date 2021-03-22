'''Elabore um programa que permita a entrada de dois valores ( x, y ), troque seus valores entre si e 
então exiba os novos resultados.'''

num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
print(num1, num2)
num1, num2 = num2, num1
print(num1, num2)