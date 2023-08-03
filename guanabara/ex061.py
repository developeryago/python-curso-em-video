t = int(input('Qual é o primero termo? '))
r = int(input('Qual é a razão? '))
cont = 1
vz = t
while cont < 11:
    print('{}'.format(vz), end='-> ')
    vz += r
    cont += 1
print('FIM')
