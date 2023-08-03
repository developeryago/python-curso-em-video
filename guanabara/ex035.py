from time import sleep
print('-=' * 20)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
print('-=' * 20)
print('ANALISANDO')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {} e {} PODEM formar um triângulo!'.format(r1,r2,r3))
else:
    print('As retas {}, {} e {} NÃO PODEM formar um triângulo!'.format(r1,r2,r3))

