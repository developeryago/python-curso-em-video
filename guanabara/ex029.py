v = int(input('A quantos km seu veículo passou no radar? '))
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Seu veículo estava acima do limite de velocidade que é de 80km/h \nVocê recebeu uma multa no valor de R${:.2f}'.format((v - 80) * 7))
print(('-' * 20), 'FIM', ('-' * 20))






