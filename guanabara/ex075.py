n1 = (int(input('Digite o 1° número: ')), int(input('Digite o 2° número: ')),
      int(input('Digite o 3° número: ')), int(input('Digite o 4° número: ')))
pares = contpares = 0
for n in n1:
    if n % 2 == 0:
        pares += n
        contpares += 1
print(f'O número 9 foi digitado {n1.count(9)} vezes \nTivemos um total de {contpares} números pares que foram {pares}')
if 3 in n1:
    print(f'E o número 3 foi digitado inicialmente na {n1.index(3) + 1}ª posição')
else:
    print('Nenhum número 3 foi digitado')


