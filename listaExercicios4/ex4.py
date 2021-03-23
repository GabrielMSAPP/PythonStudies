'''Elaborar um programa que a partir da digitação de uma frase, o programa informe quantos 
espaços em branco e quantos são, e quantas vezes aparecem cada uma das vogais a, e, i, o, u.'''

frase = input('Digite uma frase: ').lower()
vogais = ['a', 'e', 'i', 'o', 'u']
vogais_na_frase = 0
espacos_em_branco = 0
for i in frase:
    if i in vogais:
        vogais_na_frase += 1
    if i in " ":
        espacos_em_branco += 1
print(f'Numeros de vogais: {vogais_na_frase}')
print(f'Numeros de espacos em branco: {espacos_em_branco}')