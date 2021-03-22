'''Faça um programa para calcular e exibir a categoria do nadador, dado a sua idade.¶
Categoria	Faixa Etária
infantil A	de 5 a 8 anos
infantil B	de 8 a 10 anos
juvenil A	de 11 a 13 anos
juvenil B	de 14 a 17 anos
senior	maiores de 17 anos'''

idade = int(input('Informe sua idade: '))
if idade > 5 and idade <= 8:
    print('infantil A')
elif idade > 8 and idade <= 10:
    print('infantil B')
elif idade > 10 and idade <= 13:
    print(' Juvenil A')
elif idade > 13 and idade <= 17:
    print('Juvenil B')
elif idade > 17:
    print('Senior')
else:
    print('opcao invalida!!')