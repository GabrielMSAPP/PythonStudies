''' Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não. Considere que para o ano
ser bissexto basta que seja divisível por 400. Caso contrário, este precisará ser divisível por 4 e não
ser divisível por 100'''

ano = int(input('Informe o ano: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(ano, " é bissexto!")
else:
    print('O ano nao é bissexto')