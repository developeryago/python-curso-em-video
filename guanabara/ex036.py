from time import sleep
casa = float(input('Qual é o valor do imóvel que deseja comprar? R$'))
sl = float(input('Qual é o seu salário mensal? R$'))
pcl = int(input('Em quantos anos deseja pagar? '))
vpcl = casa / (pcl * 12)
print('ANALISANDO...')
sleep(3)
if vpcl < (sl * 0.3): #O valor da parcela não poderia superar 30% do salário do comprador
    print('Parabéns! Seu empréstimo foi altorizado com sucesso e você pagará {} parcelas no valor de R${:.2f}'.format(pcl,vpcl))
else:
    print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação será de R${:.2f}'
          '\nInfelizmente seu empréstimo NÃO FOI aprovado.'.format(casa,pcl,vpcl))


