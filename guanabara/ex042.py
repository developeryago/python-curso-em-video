from time import sleep
print('-=' * 20)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
print('-=' * 20)
print('ANALISANDO')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas {}, {} e {} podem formar um triângulo '.format(r1,r2,r3),end='')
    if r1 == r2 and r2 == r3: #O Python aceita simplificações nessas estruturas, portanto ficaria: r1 == r2 == r3 (sem a necessidade do 'and')
       print('EQUILÁTERO')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1: #Aqui não era necessário ter todo esse trabalho, era só por o escaleno nessa linha, e  então por um else para representar o ISÓCERES
        print('ISÓCERES')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO')
else:
    print('Os ângulos {}, {} e {} NÃO PODEM formar um triângulo!'.format(r1,r2,r3))
