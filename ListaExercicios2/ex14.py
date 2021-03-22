'''Faça um programa que leia as repostas de três questões de múltipla escolha (a, b, c, d). 
Em seguida, leia o gabarito dessas questões, ou seja, as respostas corretas. Depois, 
compare as respostas dadas com as do gabarito e indique quantas respostas estão corretas'''

respostas = []
gabarito = []
for x in range(3):
    respostas.append(str(input('Informe a resposta: ')))
for y in range(3):
    gabarito.append(str(input('Informe o gabarito: ')))
cont = 0
for x in respostas:
    print(x, '*')
    for y in gabarito:
        print(y)
        if x[respostas] == y[gabarito]:
            cont += 1
print(f'Voce acertou {cont} vezes')