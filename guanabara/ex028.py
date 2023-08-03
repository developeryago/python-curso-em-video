from random import choice #Poderia ter usado a função randint
from time import sleep #Função sleep permite simular um atraso no processamento da linha de código
n = [0,1,2,3,4,5] #Aqui ficaria randindt( 0 , 5) apenas
c =  choice(n)
print('\033[1;37m-=-' * 25)
print('\033[1;36mEscolhi um número aleatório ente 0 e 5, será que você consegue advinha-lo?')
print('\033[1;37m-=-' * 25)
chute = int(input('\033[1;36mQual número você acha que é? ')) #Jogador tentar adivinhar
print('\033[0;30;mPROCESSANDO...\033[m')
sleep(3) #Sempre na linha abaixo do local onde deseja que fique lento
if chute == c:
    print('\033[1;30;42mParabéns! Você acertou!\033[m')
else:
    str(input('\033[1;30;41mNão foi dessa vez, eu escolhi o número {}\033[m'.format(c)))












