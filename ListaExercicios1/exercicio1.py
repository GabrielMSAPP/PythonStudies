'''Faça um programa que receba três notas, calcule e mostre a média 
aritmética entre elas. Exiba, as notas, e a respectiva média.'''

notas = []
media = 0

while True:
    i = float(input('Digite uma nota: '))
    if i >= 0:
        notas.append(i)
    else:
        print("Informe um num valido!! ", end='')
    if len(notas) == 3:
        break
for i in notas:
    media += i
print(f'As notas sao{notas}')
print(f'A media das notas e: {media/3}')