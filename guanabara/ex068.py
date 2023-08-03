from random import randint
from time import sleep
contwin = 0
print('-=-' * 5, 'Jogo de PAR ou ÍMPAR', '-=-' * 5)
while True:
    pc = randint(0, 5)
    n = int(input('Qual número você escolheu: '))
    escolha = ' '
    while escolha not in 'PIPARIMPAR':
        escolha = str(input('Qual sua aposta? [P/I] ')).strip().upper()
    print('DO')
    sleep(1)
    print('LÁ')
    sleep(1)
    print('SI')
    sleep(2)
    print('JÁ!')
    if escolha == 'P' and (n + pc) % 2 == 0 or escolha == 'I' and (n + pc) % 2 == 1:
        print(f'Parabéns! Eu escolhi {pc} e a soma entre nossos números é igual a {n + pc}')
        contwin += 1
        print('Vamos jogar mais uma vez...')
        print('-=-' * 20)
    else:
        print(f'GAME OVER! \nEu escolhi {pc} e a soma deu {n + pc}\nVocê conseguiu acertar {contwin}', end= ' ' )
        print('vez seguida' if contwin == 1 else 'vezes seguidas')
        break
