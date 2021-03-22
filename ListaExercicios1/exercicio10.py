''' Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos para os quais fornece a 
quantidade de ração em gramas. Faça um programa que receba o peso do saco de ração e a quantidade de 
ração fornecida para cada gato. Calcule e mostre quanto restará de ração no saco após cinco dias'''

pesoSaco = float(input('Informe o peso do saco: '))
pesoSaco *= 1000
gato1 = float(input('Informe a qtd para gato1: '))
gato2 = float(input('Informe a qtd para gato2: '))
gastos = (gato1 + gato2) * 5
print(f'A quantidade restante é: {pesoSaco - gastos}')