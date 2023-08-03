from time import sleep
cont18 = homens = mulheres = 0
while True:
    print('-=-' * 10, 'CADASTRE UMA PESSOA', '-=-' * 10)
    id = int(input('Qual a sua idade? '))
    sexo = r = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if id > 18:
        cont18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and id < 20:
        mulheres += 1
    if r == 'N':
        break
print('ANALISANDO...')
sleep(2)
print('-=-' * 27)
print(f'Considerando os dados: \n{cont18} pessoas tem mais de 18 anos \n{homens} são homens \n{mulheres} mulheres tem menos de 20 anos')
print('-=-' * 11, 'FIM DO PROGRAMA', '-=-' * 11)

