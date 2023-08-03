lista = []
while True:
    lista.append(int(input('Digite um número para adicionar a lista: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'Você digitou um total de {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Que ordenados em ordem decrescente temos: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes')
else:
    print('Não identificamos o valor 5 nessa lista')
