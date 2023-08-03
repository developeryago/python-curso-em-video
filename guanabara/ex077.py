lista = ('batata', 'bolo', 'whey', 'ceatina', 'betalanina')
for p in lista:
    print(f'\nNa palava {p} temos as vogais ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end= ' ')
