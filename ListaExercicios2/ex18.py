'''Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B 
e apresentar o resultado da diferença do maior valor pelo menor'''

A = int(input('Informe um numero:'))
B = int(input('Informe um numero:'))
if A > B:
    print(f'A diferença entre os numeros é: {A - B}')
else:
    print(f'A diferença entre os numeros é: {B-A}')