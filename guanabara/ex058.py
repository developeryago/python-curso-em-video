from random import randint
from time import sleep #Função sleep permite simular um atraso no processamento
tentativas = 1
pc = randint(0, 10)
print('\033[1;37m-=-' * 25)
print('\033[1;36mEscolhi um número aleatório ente 0 e 10, será que você consegue advinha-lo?')
print('\033[1;37m-=-' * 25)
chute = int(input('\033[1;36mFaça seu palpite: ')) #Jogador tentar adivinhar
print('\033[1;37mPROCESSANDO...\033[m')
sleep(1) #Sempre na linha abaixo do local onde deseja que fique lento
while chute != pc:
    tentativas += 1
    if pc > chute: #Computador dá dicas
        chute = int(input('\033[1;31mMAIS... tente novamente: \033[m'))
    elif pc < chute:
        chute = int(input('\033[1;31mMENOS... tente novamente: \033[m'))
print('\033[1;32mParabéns! Você acertou na {}ª tentativa!\033[m'.format(tentativas))












