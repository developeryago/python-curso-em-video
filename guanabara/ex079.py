lista = []
while True:
     n = (int(input('Digite um valor para adicionar a lista: ')))
     r = ' '
     if n not in lista:
         lista.append(n)
         print('Valor adicionado com sucesso')
     else:
         print('Valor duplicado, não irei adiciona-lo')
     while r not in 'SN':
         r = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
     if r == 'N':
         break
lista.sort()
print(f'Você adicionou os valores {lista}')

