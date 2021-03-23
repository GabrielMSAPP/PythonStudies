'''Faça um programa que leia uma lista com dez caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.'''

vogais = ['a', 'e', 'i', 'o', 'u']
lista = []
j = 0
for i in range(10):
    caracter = input('Digite um caracter: ')
    caracter = caracter.lower()
    if caracter in vogais:
        pass
    else:
        lista.append(caracter)
        j += 1
print(f'Foram inseridas {j} consoantes, são elas {lista}')