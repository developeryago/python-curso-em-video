from random import randint
lista = []
jogos = int(input(f'Quantos jogos deseja fazer? '))
while jogos > 0:
    sugestao = randint(1, 60)
    for n in lista:
        if n not in lista:
            lista.append(sugestao)
        else:
            lista.append(randint(1, 60))
    jogos -= 1
print(lista)
