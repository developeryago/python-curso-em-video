soma = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
print('A soma entre os números é {}'.format(soma))

