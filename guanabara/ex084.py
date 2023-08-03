lista = []
listaleves = []
listapesadas = []
contn = 0
while True:
    n = lista.append(str(input('Digite seu nome: ')))
    peso = lista.append(float(input('Digite seu peso: ')))
    contn += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 20)
    if r == 'N':
        break
print(f'Tivemos um total de {contn} pessoas cadastradas')
for p in lista:
    if p >= 100:
        listapesadas.append(p)
    else:
        listaleves.append(p)
print(f'As mais leves cadastradas foram{listaleves}')
print(f'E as mais pesadas foram {listapesadas}')

