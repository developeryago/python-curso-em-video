from random import randint
lista = (randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50), randint(0, 50))
contlista = sorted(lista)
print(f'Os valores escolhidos aleatoriamente foram {lista}, dessa forma: '
      f'\nO menor valor foi {contlista[0]}\nE o maior valor foi {contlista[-1]}')
# Para descobrir o maior valor poderia ter utilizado o comando max(lista)
# E para o menor valor poderia ter usado o comando min(lista)
