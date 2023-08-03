f = str(input('Escreva uma frase: ')).strip().lower()
print('-'*40)
print('A letra A aparece {} vezes \nA primeira letra A apareceu na posição {} \nA última letra A apareceu na posção {}'.format(f.count('a'),f.find('a')+1,f.rfind('a')+1))
print('-'*40)

#print('A letra A aparece {} vezes'.format(f.count('a')))
#print('A primeira letra A apareceu na posição {}'.format(f.find('a')+1))
#print('A última letra A apareceu na posção {}'.format(f.rfind('a')+1))



