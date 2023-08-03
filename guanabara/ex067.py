while True:
    n = int(input('Digite um número para visualizar sua tabuada [ou um número >0 para parar]: '))
    print('-=-' * 10)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} X {n} = {c * n}')
    print('-=-' * 10)
print('-----FIM-----')
