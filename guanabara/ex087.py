lista = []
listab = []
listac = []
soma = maiorlistab = 0
for c in range(1, 4):
    a = lista.append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(1, 4):
    b = listab.append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(1, 4):
    cc = listac.append(int(input(f'Digite um valor para [2, {c}]: ')))
print('-=' * 20)
print('Sua Matríz (3/3):')
print(f'[{lista[0]}], [{lista[1]}], [{lista[2]}]')
print(f'[{listab[0]}], [{listab[1]}], [{listab[2]}]')
print(f'[{listac[0]}], [{listac[1]}], [{listac[2]}]')
for n in lista:
    if n % 2 == 0:
        soma += n
for n in listab:
    if n % 2 == 0:
        soma += n
for n in listac:
    if n % 2 == 0:
        soma += n
if listab[0] > listab[1] and listab[0] > listab[2]:
    maiorlistab = listab[0]
elif listab[1] > listab[2] and listab[1] > listab[0]:
    maiorlistab = listab[1]
else:
    maiorlistab = listab[2]
print(f'A soma ente os PARES é {soma}')
print(f'A soma entre os valores da 3ª coluna é {lista[2] + listab[2] + listac[2]}')
print(f'O maior valor da segunda linha é {maiorlistab}')
