d = int(input('Quantos km você percorrerá em sua viagem? '))
if d <= 200:
    print('Baseado nisso, o preço da sua passagem será R${:.2f}'.format(d * 0.5))
else:
    print('Nesse caso, o preço da sua passagem será R${:.2f}'.format(d * 0.45))

