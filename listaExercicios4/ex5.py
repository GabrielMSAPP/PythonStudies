'''Faça um programa que leia um número de telefone, e corrija o número no caso deste conter 
somente 7 dígitos, acrescentando o ’3’ na frente. O usuário pode informar o número com ou 
sem o traço separador'''

telefone = input('Digite um telefone: ')
traco = False
for i in telefone:
    if i == '-':
        traco = True
if len(telefone) == 7 or len(telefone) == 8 and traco:
    telefone = '3' + telefone
print(f'Seu telefone é: {telefone}')