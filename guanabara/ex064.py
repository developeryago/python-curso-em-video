contn = n = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        contn += 1
        soma += n
print('Voce digitou {} números e a soma deles dá {}'.format(contn, soma))
