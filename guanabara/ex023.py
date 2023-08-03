num = int(input('Escreva um número de até 4 dígitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o n° {}'.format(num))
print('-' * 20)
print('Unidade {} \n Dezena {} \n Centena {} \n Milhar {}'.format(u,d,c,m))
print('-' * 20)
