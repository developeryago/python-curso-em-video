lista = []
listab = []
listac = []
for c in range(1, 4):
    lista.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(1, 4):
    listab.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(1, 4):
    listac.append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 20)
print(f'[{lista[0]}], [{lista[1]}], [{lista[2]}]')
print(f'[{listab[0]}], [{listab[1]}], [{listab[2]}]')
print(f'[{listac[0]}], [{listac[1]}], [{listac[2]}]')
