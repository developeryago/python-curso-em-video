lista = []
for cont in range(1, 6):
    lista.append(int(input(f'Digite o {cont}º valor: ')))
print(f'O maior número digitado foi {max(lista)} que está nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {min(lista)} que está nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')

