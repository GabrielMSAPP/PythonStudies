'''Elabore um programa que efetue a leitura de quatro notas reais, adicione-as a uma lista e mostre-as,
inclusive a média aritmética, arredondar duas casas decimais. Verifique e exiba as devidas mensagens se 
o aluno está aprovado ou não, considerando que a média de aprovação é maior ou igual a 7.0, e em prova exame,
se média aritmética entre 4.0 e menor que 7.0. E reprovado, se menor que 4.0.'''

lista = []
soma = 0
for i in range(4):
    nota = float(input('Digite sua nota: '))
    soma = soma + nota
    lista.append(nota)
    media = round(soma / 4, 2)
print(f'Suas notas são {lista}sendo assim sua média é {media}')
if media >= 7:
    print('Você está aprovado')
elif 4 <= media < 7:
    print('Pegou exame')
else:
    print('Reprovou')