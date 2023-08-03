t1 = 0
t2 = 1
t3 = 0
t4 = 3
print('-=-' * 10)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-' * 10)
n = int(input('Digite quantos termos deseja visualizar: '))
print('{}-> {}'.format(t1, t2), end='-> ')
while t4 <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    t4 += 1
    print('{}'.format(t3), end='-> ')
print('\033[31mFIM')

