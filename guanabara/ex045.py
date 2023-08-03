from random import randint
from time import sleep
a = ('Pedra', 'Papel','Tesoura') #Variável lista
'''pc = choice(a)''' #Deveria ter usado randint (Máquina faz sua escolha)
pc = randint(0, 2)
print('-=' * 22)
print('Bem-vindo ao jogo de Pedra, Papel e Tesoura!\nSuas Opções:\n[1] Pedra\n[2] Papel\n[3] Tesoura')
print('-=' * 22)
jogador = int(input('Faça sua jogada: ')) #Jogador faz sua escolha
str(print('JO'))
sleep(1)
str(print('KE'))
sleep(1)
str(print('PO'))
if pc == 0: #Jogou Pedra
    if jogador == 1:
        print('Empate! Eu também escolhi {}'.format(a[pc]))
    elif jogador == 2:
        print('Parabéns! Você venceu, eu escolhi {}'.format(a[pc]))
    elif jogador == 3:
        print('Você perdeu, eu escolhi {}'.format(a[pc]))
    else:
        print('Escolha INVÁLIDA! Tente novamente')
if pc == 1:  # Jogou Papel
    if jogador == 1:
        print('Você perdeu, eu escolhi {}'.format(a[pc]))
    elif jogador == 2:
        print('Empate! Eu também escolhi {}'.format(a[pc]))
    elif jogador == 3:
        print('Parabéns! Você venceu, eu escolhi {}'.format(a[pc]))
    else:
        print('Escolha INVÁLIDA! Tente novamente')
if pc == 2:  # Jogou Tesoura
    if jogador == 1:
        print('Parabéns! Você venceu, eu escolhi {}'.format(a[pc]))
    elif jogador == 2:
        print('Você perdeu, eu escolhi {}'.format(a[pc]))
    elif jogador == 3:
        print('Empate! Eu também escolhi {}'.format(a[pc]))
    else:
        print('Escolha INVÁLIDA! Tente novamente')


