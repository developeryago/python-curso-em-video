s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    cont = cont + 1
    if n % 2 == 0:
        s = s + n
'''print(s)''' #Forma como pensei em expressar o resultado
print('Você informou {} valores e o resultado da soma dos numeros pares foi {}'.format(cont, s))




