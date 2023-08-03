print('Vamos descobrir quanto você terá que pagar pelo produto desejado!')
preço = float(input('Qual é o valor do produto? '))
print('CONDIÇÃO DE PAGAMENTO')
print('[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
condição = int(input('Qual é a condição de pagamento? '))
if condição == 1:
    print('Devido a sua forma de pagamento você terá 10% de desconto no valor do porduto, passando a pagar R${:.2f}!'.format(preço - (preço * 0.1)))
elif condição == 2:
    print('Devido a sua forma de pagamento você terá 5% de desconto no valor do porduto, passando a pagar R${:.2f}!'.format(preço - (preço * 0.05)))
elif condição == 3:
    print('Você pagará o preço normal de R${:.2f} em 2x SEM JUROS!'.format(preço))
elif condição == 4:
    parcela = int(input('Qual o total de parcelas? '))
    totalparcela = (preço + (preço * 0.2)) / parcela
    print('Sua compra será parcelada em {}X de R${:.2f}!'.format(parcela,totalparcela))
else:
    print('Escolha INVÁLIDA!')


