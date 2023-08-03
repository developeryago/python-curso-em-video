s = int(input('Qual o seu salário atual? '))
if s <= 1250:
    print('Seu salário de R${:.2f} terá um acrescimo de 15%, com isso passará a ganhar R${:.2f} por mês'.format(s, (s * 0.15) + s))
else:
    print('Seu salário de R${:.2f} terá um acrescimo de 10%, com isso passará a ganhar R${:.2f} por mês'.format(s, (s * 0.10) + s))
