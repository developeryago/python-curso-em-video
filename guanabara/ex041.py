from datetime import date
a = int(input('Em qual ano você nasceu? '))
id = date.today().year - a
if id <= 9: #Poderia ter elaborado as condições apenas para dizer qual categoria a pessoa se enquadra, já que o print(idade) é igual em todos
    print('Você possui {} anos e se enquadra na cetegoria MIRIM'.format(id))
elif id <= 14:
    print('Você possui {} anos e se enquadra na cetegia INFANTIL'.format(id))
elif id <= 19:
    print('Você possio {} anos e se enquadra na categoria JÚNIOR'.format(id))
elif id <= 25:
    print('Você possui {} anos e se enquadra na categoria SÊNIOR!'.format(id))
else:
    print('Você possui {} anos e se enquadra na cetegoria MASTER!'.format(id))

