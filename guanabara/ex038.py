n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
if n1 > n2:
    print('O número {} foi o PRIMEIRO a ser digitado e ele é o maior!'.format(n1))
elif n1 < n2:
    print('O número {} foi o SEGUNDO a ser digitado e ele é o maior!'.format(n2))
else:
    print('Os números possuem o MESMO VALOR!')
