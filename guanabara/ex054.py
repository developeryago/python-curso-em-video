from datetime import date
from time import sleep
maior = 0
menor = 0
for c in range(1, 8):
    id = int(input('Em qual ano {}ª pessoa nasceu? '.format(c)))
    ano = date.today().year - id
    if ano >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
sleep(1)
print('Essa lista possui {} maiores de idade e {} menores de idade'.format(maior, menor))


