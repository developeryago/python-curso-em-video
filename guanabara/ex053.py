f = str(input('Digite uma frase: ')).strip().upper()
sep = f.split()
junt = ''.join(sep)
inverso = ''
for c in range(len(junt) - 1, -1, -1):
    inverso += junt[c]
print('O Inverso de {} é {}'.format(junt, inverso), end=' ')
if inverso == junt:
    print('\nEssa frase é um palíndromo!')
else:
    print('\nEssa frase não é um palíndromo!')
