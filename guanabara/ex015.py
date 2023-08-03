c = int(input('Por quantos dias o carro foi alugado? '))
d = float(input('Quantos km ele percorreu? '))
print('O total a pagar pelo aluguel do carro é R${:.2f}'.format((c * 60) + (d * 0.15)))
