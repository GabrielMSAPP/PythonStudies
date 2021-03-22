'''Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula:
prestacao = valor + (valor (taxa / 100) tempo)'''

valor = float(input('Informe o valor da parcela: '))
tempo = int(input('Informe o tempo de atraso: '))
taxa = float(input('Informe o valor da taxa: '))
print(f'O valor da prestação é: {valor+(valor*(taxa/100)*tempo)}')