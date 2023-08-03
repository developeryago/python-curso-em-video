lista = []
listapar = []
listaimpar = []
while True:
    n = lista.append(int(input('Digite um número para adicionar a lista: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
print(f'Os valores digitados foram {lista} \nSendo: \n{listapar} PARES '
      f'\n{listaimpar} ÍMPARES')
