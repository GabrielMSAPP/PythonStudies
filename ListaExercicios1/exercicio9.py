'''Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária. 
Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
Sabe-se que cada operação bancária de retirada paga CPMF de 0,38% e o saldo inicial da conta está zerado'''

saldoConta = float(input('Informe o saldo da conta: '))
cheque1 = float(input('Informe o  valor do cheque que queira depositar: '))
cheque2 = float(input('Informe o  valor do cheque que queira depositar: '))
print(f'O saldo da sua conta é: {saldoConta - cheque1 - cheque2 - cheque1*0.38/100 - cheque2*0.38/100}')