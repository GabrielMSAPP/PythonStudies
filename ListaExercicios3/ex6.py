'''Faça um programa que apresente a soma dos cem primeiros números naturais (1+2+3+4+5+...+98+99+100).'''

soma = 0
for contador in range(1, 101):
    soma += contador
print(f'A soma dos cem primeiros números naturais é: {soma}')