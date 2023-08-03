lista = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        lista.insert(lista[0], n)
    else:
        lista.insert(lista[1], n)
print(lista)
