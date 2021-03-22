'''Faça um programa que calcule o IMC de uma pessoa (IMC = massa em kg / altura em metros elevado ao quadrado) e informe a sua classificação segundo a tabela a seguir:¶
IMC	Classificação
Menor que 17.0	Muito abaixo do peso
De 17.0 a 18.50	Abaixo do peso
De 18.50 a 25.0	Peso normal
De 25.0 a 30.0	Acima do peso
De 30.0 a 35.0	Obesidade I
De 35.0 a 40.0	Obesidade II
Acima de 40.0	Obesidade III (mórbida)'''

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/altura**2
if imc < 17:
    print('Muito abaixo do peso')
elif imc >= 17 and imc < 18.50:
    print('Abaixo do peso')
elif imc >= 18.50 and imc < 25:
    print('Peso normal')
elif imc >= 25 and imc < 30:
    print('Acima do peso')
elif imc >= 30 and imc < 35:
    print('Obesidade I')
elif imc >= 35 and imc < 40:
    print('Obesidade II')
elif imc > 40:
    print('Obesidade III (MORBIDA)')