'''Faça um programa que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:¶
a hora trabalhada vale a metade do salário mínimo;
o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
o imposto equivale a 3% do salário bruto;
o salário a receber equivale ao salário bruto menos o imposto'''

horasTrabalhadas = float(input('Informe as horas trabalhadas: '))
salarioMin = float(input('Informe o salario minimo: '))
bruto = horasTrabalhadas * salarioMin/2
print(f'O salario a receber é: {bruto - (bruto * 3/100)}')