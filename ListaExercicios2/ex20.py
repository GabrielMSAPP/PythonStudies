'''Ler os valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3, N4.
Calcular a média aritmética (variável MD1) desse aluno e apresentar a mensagem "APROVADO" se a média obtida for
maior ou igual a 7. Caso contrário, o programa deve solicitar a quinta nota (nota de exame, representada
pela variável NE) do aluno e calcular uma nova média aritmética (variável MD2) entre a nota de exame e 
a primeira média aritmética. Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem
"APROVADO EM EXAME". Caso contrário, apresentar a mensagem "REPROVADO". Informar também, após a apresentação
 das mensagens, o valor da média obtida pelo aluno.'''

N1, N2, N3, N4 = float(input('Informe sua nota: ')), float(input('Informe sua nota: ')), float(
    input('Informe sua nota: ')), float(input('Informe sua nota: '))
MD1 = (N1 + N2 + N3 + N4)/4
NE = 0
MD2 = 0
if MD1 >= 7:
    print(f'Aprovado sua media foi {MD1}')
else:
    NE = float(input('Informe sua quinta nota:'))
    MD2 = (MD1 + NE)/2
    if MD2 >= 5:
        print(f'Aprovado em exame sua media foi {MD2}')
    else:
        print(f'Reprovado sua media foi {MD2}')