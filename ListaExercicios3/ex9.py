'''Faça um programa que leia quinze valores numéricos inteiros e no final 
apresente o somatório e a média aritmética dos valores lidos'''

soma = 0
for contador in range(1, 16):
    numero = int(input(f'Insira o {contador}o. numero: '))
    soma += numero
media = soma / 15
print(f'Média aritmética dos valores lidos: {media}')