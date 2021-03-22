'''Uma empresa de ônibus com 48 poltronas (24 nas janelas e 24 no corredor). Faça um programa 
que controle o uso das poltronas ocupadas no corredor e na janela. Considere que 0 representa poltrona
desocupada e 1, poltrona ocupada. Inicialmente, todas as poltronas estarão livres. Depois disso, 
o programa deverá exibir as seguintes opções:
1 - Vender passagens
2 - Mostrar mapa de ocupações do ônibus
Quando a opção escolhida for Vender passagens, deverá ser perguntado se o usuário deseja janela ou corredor
e o número da poltrona.
O programa deverá dar uma das seguintes mensagens:
Venda efetivada (se a poltrona solicitada estiver livre, marcando-a como ocupada).
Poltrona ocupada (se a poltrona não estiver disponível para a venda).
Ônibus lotado (quando todas as poltronas estiverem ocupadas).'''

corredor = list()
janelas = list()
for contador in range(1, 49):
    if contador % 2 == 0:
        corredor.append(contador)
    else:
        janelas.append(contador)
while True:
    print(f'{" MENU ":-^40}')
    print(f'1 - Vender passagens.\n'
          f'2 - Mostrar poltronas ocupadas.\n'
          f'3 - Sair.\n')
    escolha = int(input('Digite a opção: '))
    if escolha == 3:
        break
    elif escolha == 1:
        while True:
            comprar = int(input('Insira o numero de uma poltrona: '))
            if comprar in janelas:
                confirmar = str(input(f'Confirma a compra da poltrona'
                                      f' {comprar}? s/n')).strip().lower()[0]
                if confirmar == 's':
                    janelas.remove(comprar)
                    break
                elif comprar in corredor:
                    confirmar = str(input(f'Confirma a compra da poltrona'
                                          f' {comprar}? s/n')).strip().lower()[0]
                    if confirmar == 's':
                        corredor.remove(comprar)
                    break
                else:
                    print('Não encontrado, tente novamente!')
                    input('Pressione qualquer tecla para continuar!')
    elif escolha == 2:
        print(f'{" JANELA ":-^40}')
        for cadeira in janelas:
            print(cadeira, end=' - ')
            if cadeira % 10 == 1:
                print()
            print()
            print(f'{" CORREDOR ":-^40}')
            for cadeira in corredor:
                print(cadeira, end=' - ')
                if cadeira % 10 == 0:
                    print()
            print()
            input('Pressione qualquer tecla para continuar!')
        else:
            print('Erro, tente novamente: ')