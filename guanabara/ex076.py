lista = ('Carro', 5000,
         'Iphone', 2000,
         'Relógio', 175)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end='')
    else:
        print(f'R${lista[c]:.2f}')



