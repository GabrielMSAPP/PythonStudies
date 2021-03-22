'''Faça um programa que receba três notas e seus respectivos pesos, 
calcule e mostre a média ponderada dessas notas. Exiba, as notas, seus respectivos pesos e a média.'''

media = 0
n1 = float(input('Digite 1º nota: '))
n2 = float(input('Digite 2º nota: '))
n3 = float(input('Digite 3º nota: '))
p1 = float(input('Digite o peso da n1: '))
p2 = float(input('Digite o peso da n2: '))
p3 = float(input('Digite o peso da n3: '))

print(f'As notas sao: {n1, n2, n3} com os determinados pesos {p1, p2, p3}')
print(f'A media ponderada é: {(n1*p1+n2*p2+n3*p3)/(p1+p2+p3)}')