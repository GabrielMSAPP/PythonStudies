'''Sabendo que a relação entre vértices, arestas e faces de um objeto geométrico é dada pela fórmula:
vértices + faces = arestas + 2. Elabore um programa que calcule o número de vértices de um objeto 
geométrico genérico. A entrada será o número de faces e arestas (dadas por um número inteiro e positivo) 
e a saída será o número de vértices'''

faces = int(input('Informe o numero de faces: '))
arestas = int(input('Informe o numero de arestas: '))
if faces and arestas > 0:
    print(f'O numero de vertices sao: {arestas+2 - faces}')
else:
    print('Informe um valor positivo para ambos.')