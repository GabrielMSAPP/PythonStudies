'''Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável N
e apresentar o valor lido como sendo positivo. Dica: se o valor lido for menor que zero,
o mesmo deve ser multiplicado por -1'''

N = int(input('Informe um numero: '))
if N < 0:
    print(N*-1)
else:
    print(N)