'''Dado um polígono convexo de n lados, podemos calcular o número de diagonais diferentes (nd) desse polígono 
pela fórmula: nd = n * (n - 3) / 2. Fazer um programa que leia quantos lados tem o polígono,
calcule e escreva o número de diagonais diferentes (nd) do mesmo'''
n = int(input("Informe o número de lados: "))
print(n, "lados dá", n*(n - 3)/2, "diagonais")