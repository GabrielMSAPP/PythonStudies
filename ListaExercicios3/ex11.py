'''Faça um algoritmo que apresente todos os valores numéricos divisíveis por 4 e menores que 200'''
for contador in range(0, 201):
    if contador % 4 == 0:
        print(contador, end=', ')
print('FIM')