'''Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, 
todos incorporam essa palavra em seu vocabulário. Sabendo-se que 100 quilowatts de energia custa 
um sétimo do salário mínimo, fazer um programa que receba o valor do salário mínimo e a 
quantidade de quilowatts gasta por uma residência e calcule. Imprima:
o valor em reais de cada quilowatt,
o valor em reais a ser pago,
o novo valor a ser pago por essa residência com um desconto de 10%.'''

salarioMin = float(input('Informe o salario minimo: '))
qlwCasa = float(input('Informe a quantidade gasta de quilowatts gasta: '))
preco = (salarioMin/7)/100
print(f'O valor a ser pago é: {qlwCasa * preco:.2f}')
print(
    f'O valor com desconto é: {qlwCasa * preco - ((qlwCasa * preco) * 10/100):.2f}')