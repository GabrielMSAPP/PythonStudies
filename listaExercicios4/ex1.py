'''Elabore um programa que efetue a leitura de duas strings e informe o seu conteúdo, seguido de seu 
comprimento. Indique também se as duas strings possuem o mesmo comprimento e se são iguais ou diferentes no
conteúdo'''

dicionario = {}
for i in range(2):
    palavra = input('Digite uma palavra: ')
    dicionario[i] = [palavra, len(palavra)]
    print(dicionario)
if dicionario[0][0] == dicionario[1][0]:
    print('Conteúdo iguais')
if dicionario[0][1] == dicionario[1][1]:
    print('Comprimento iguais')