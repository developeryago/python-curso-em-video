totalgasto = maisdemil = contbarato = 0
maisbarato = ' '
while True:
    n = str(input('Digite o nome do produto: ')).strip().title()
    vl = float(input('Qual seu valor? R$'))
    r = ' '
    totalgasto += vl
    contbarato += 1
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if vl > 1000:
        maisdemil += 1
    if contbarato == 1 or vl < contbarato:
        contbarato = vl
        maisbarato = n
    if r == 'N':
        break
print('-=-' * 10, 'FIM DO PROGRAMA', '-=-' * 10)
print(f'O valor total da compra foi de R${totalgasto:.2f} \n{maisdemil} produtos custam mais de R$1000,00 '
      f'\nE {maisbarato} que custa R${contbarato:.2f} é o produto mais barato')
