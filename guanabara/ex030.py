n = int(input('Escreva um número: '))
'''par = [0,2,4,6,8,10] Tentativa de formar uma lista com números pares
impar = [1,3,5,7,9]     Tentativa ímpar
u = n // 1 % 10         Tantativa de usar a únidade para considerar se é par ou ímpar 
if u == (par):
    print('O número que você escreveu é par')
else:
    print('O número que você escreveu é ímpar')'''
r = n % 2 #O resto da divisão de qualquer nº par por 2 sempre dará 0  e se for ímpar dará 1
if r == 0:
    print('Você escolheu o número {} e ele é PAR'.format(n))
else:
    print('Você escolheu o número {} e ele é ÍMPAR'.format(n))
