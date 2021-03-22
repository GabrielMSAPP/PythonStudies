'''Elabore um programa que calcule e exiba a média aritmética de 5 números ( k, x, y, z, w).'''

media = 0
for i in range(5):
    i = float(input('Informe um numero: '))
    media += i
print(f'A media aritmetica dos numeros sao: {media/5}')