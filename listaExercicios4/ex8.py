'''Elabore um programa que efetue a leitura de quinze números inteiros, adicione-os a 
uma lista e mostre-a de forma invertida, do último para o primeiro'''

lista = []
for i in range(15):
    numero = int(input('Digite o um número: '))
    lista.append(numero)
print(lista[::-1])