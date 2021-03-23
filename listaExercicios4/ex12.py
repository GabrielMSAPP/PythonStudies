'''Elabore um programa que efetue a leitura de quatro notas reais de10 alunos, calcule e armazene
em uma lista, a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0'''

lista = []
k = 0
for i in range(1, 11):
    soma = 0
    for j in range(1, 5):
        nota = float(input(f'Digite a {j}ª nota do aluno "{i}\n'))
        soma = soma + nota
        media = soma / 4
        lista.append(media)
        if media >= 7:
            k += 1
print(f'A média dos 10 alunos eh {lista} sendo {k} acima da média')