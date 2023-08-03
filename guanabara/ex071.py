n = int(input('Qual valor deseja sacar? R$'))
tot = n
contced = 0
ced = 200
while True:
    if tot >= ced:
        tot -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} de R${ced}')
        elif ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if tot == 0:
            break
print('FIM')

