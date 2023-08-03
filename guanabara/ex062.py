t = int(input('Qual é o primero termo? '))
r = int(input('Qual é a razão? '))
cont = 1
vz = t
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(vz), end='-> ')
        vz += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja ver a mais? '))
print('Você exibiu um total de {} termos dessa P.A.'.format(total))