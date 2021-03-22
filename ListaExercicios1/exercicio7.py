'''Elaborar um programa que calcule e apresente em metros por segundo o valor da 
velocidade de um projétil quepercorre uma distância em quilômetros a um espaço de tempo em minutos'''

tempoGasto = float(input('Informe o tempo gasto: '))
distancia = float(input('Informe a distancia: '))
print(f'A velocidade que o projetil atingiu foi: {distancia*1000/tempoGasto*60}')