contn = maiorvalor = valortotal = menorvalor = med = 0
r = ''
while r != 'N':
    n = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
    contn += 1
    valortotal += n
    med = valortotal / contn
    if contn == 1:
        maiorvalor = menorvalor = n
    else:
        if n < menorvalor:
            menorvalor = n
        if n > maiorvalor:
            maiorvalor = n
print('Você digitou {} valores, a média entre eles foi {:.2f}, o maior valor foi {} e o menor valor foi {}'.format(contn, med, maiorvalor, menorvalor))
