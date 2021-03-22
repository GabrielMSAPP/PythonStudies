'''Elabore um programa que calcule e exiba quantas notas de 50, 10 e 1 
são necessárias para se pagar uma conta cujo valor é fornecido'''

conta = float(input('Informe o valor da conta: '))
d50, d10, d1 = 0, 0, 0
while conta >= 50:
    d50 += 1
    conta -= 50
while conta >= 10:
    d10 += 1
    conta -= 20
while conta >= 1:
    d1 += 1
    conta -= 20
print(f'A quantidade de notas fornecidas é: \n50$ - {d50} \n10$ - {d10} \n1$ - {d1}')