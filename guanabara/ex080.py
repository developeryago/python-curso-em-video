lista = []
for vl in range(1, 6):
    r = (int(input(f'Digite o {vl}º valor: ')))
    if vl == 1 or r > lista[-1]:
        lista.append(r)
        print('Adiconado os final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if r < lista[pos]:
                lista.insert(pos, r)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
    '''if vl == 2:
        if r < lista[0]:
            lista.insert(0, r)
        else:
            lista.insert(1, r)
    if vl == 3:
        if r < lista[0]:
            lista.insert(0, r)
        elif r < lista[1]:
            lista.insert(1, r)
        else:
            lista.insert(2, r)
    if vl == 4:
        if r < lista[0]:
            lista.insert(0, r)
        elif r < lista[1]:
            lista.insert(1, r)
        elif r < lista[2]:
            lista.insert(2, r)
        else:
            lista.insert(3, r)
    if vl == 5:
        if r < lista[0]:
            lista.insert(0, r)
        elif r < lista[1]:
            lista.insert(1, r)
        elif r < lista[2]:
            lista.insert(2, r)
        elif r < lista[3]:
            lista.insert(3, r)
        else:
            lista.insert(4, r)'''
print(f'Você digitou os valores {lista}')


