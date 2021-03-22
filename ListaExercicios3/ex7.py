'''Faça um programa que apresente os resultados da soma e da média
aritmética dos valores pares situados na faixa numérica de 50 a 70.'''

soma = quantidade = 0
for contador in range(50, 71):
    soma += contador
    quantidade += 1
media = soma / quantidade
print(f'A média é igual a {media}')