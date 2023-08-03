smid = 0
idademaisvelho = 0
nomemaisvelho = ''
mulheres = 0
for c in range(1, 5):
        print('-----{}ª PESSOA-----'.format(c))
        n = str(input('Nome: ')).strip().title()
        id = int(input('Idade: '))
        sex = str(input('Sexo? [M/F]: ')).strip().upper()
        smid += id
        if sex == 'M' and id > idademaisvelho:
                nomemaisvelho = n
                idademaisvelho = id
        if sex == 'F' and id < 20:
                mulheres += 1
med = smid / 4
print('A média de idade do grupo é {} anos'.format(med))
print('O homem mais velho é {} e ele tem {} anos'.format(nomemaisvelho, idademaisvelho))
print('Um total de {} mulheres tem menos de 20 anos'.format(mulheres))


