'''Criar um programa que efetue o cálculo da hora aula líquida (descontado o percentual de imposto) 
de um professor. Os dados fornecidos serão: valor da hora aula, número de aulas dadas no mês e 
percentual de desconto do INSS.'''

horaAula = float(input('Informe o valor da hora aula: '))
numAulas = float(input('Informe o numero de aulas dadas: '))
desc = float(input('Informe o percentual de desconto no mes: '))
print(f'O  valor da hora aula liquida é: {(horaAula*numAulas) * desc/100}')