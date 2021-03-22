'''Faça um programa para calcular e exibir a valor do imposto de ICMS de um produto, conforme a classificação do tipo de produto e do valor de custo do mesmo digitado pelo usuário (incluindo centavos – cuidado com o uso do tipo de dados correto).¶
Classificação do Produto	Porcentagem de ICMS
Cesta básica	isento
Eletrônicos	25%
Serviços	18%
Os demais produtos	12%'''

print(' 1 - cesta basica')
print(' 2 - eletronicos')
print(' 3 - serviços')
print(' 4 - demais produtos')
opc = int(input('Informe a classificação do produto:'))
valor = float(input('Informe o valor do produto: '))
if opc == 1:
    print('isento de imposto!')
elif opc == 2:
    print(f'imposto de {valor * 25/100}')
elif opc == 3:
    print(f'imposto de {valor * 18/100}')
elif opc == 4:
    print(f' imposto de {valor * 12/100}')