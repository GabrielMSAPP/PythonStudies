'''Faça um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 2000'''

for contador in range(0, 2001):
    if contador % 2 == 1:
        print(contador, end=', ')
print('FIM')