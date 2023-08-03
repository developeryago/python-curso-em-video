n = int(input('Digite um número para descobrir seu fatorial: '))
cont = n
fatorial = 1
while cont > 0:
    print(cont, end='')
    print(' X ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))





# print('\n{}! é igual à: '.format(n))
