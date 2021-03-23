''' Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as
letras embaralhadas. O programa terá uma lista de palavras lidas de uma lista a ser fixada inicialmente 
pelo programador e escolherá uma aleatoriamente. O jogador terá uma única tentativa para adivinhar a palavra.
Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
Observação: Refaça, possibilitando ao jogador tentar até 5 vezes'''

import random
animais = ['gato', 'cachorro', 'cavalo', 'jumento', 'peixe',
           'zebra', 'papagaio', 'girafa', 'pomba', 'lagosta']
escolhida = random.choice(animais)
shuffled = list(escolhida)
random.shuffle(shuffled)
shuffled = "".join(shuffled)
print(f'A palavra embaralhada é {shuffled}\n')
tentativa = input('Qual a palavra embaralhada? ')
if escolhida == tentativa.lower():
    print('Você acertou, parabéns')
else:
    print('Você errou')
print(f'A palavra era {escolhida}')