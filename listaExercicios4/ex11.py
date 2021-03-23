'''Faça um programa que leia 15 números inteiros e armazene-os em uma lista NUMEROS. 
Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima os três vetores'''

numeros = []
par = []
impar = []
for i in range(10):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(f'Os números digitados foram {numeros}\n'
      f'Dentre eles esses são pares {par} e estes são ímpares {impar}')