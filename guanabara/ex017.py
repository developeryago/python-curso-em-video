'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto ajacente: '))
hi = (co ** 2) + (ca ** 2) ** (1/2)
print('A hipotenusa vale {:.2f}'.format(hi))'''

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vale {:.2f}'.format(hi))


