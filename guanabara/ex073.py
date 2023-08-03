from time import sleep
print('-=-' * 10)
print('Tabela do Brasileirão Assaí 2022')
print('-=-' * 10)
classificacao = ('Palmeiras', 'Inter', 'Fluminense', 'Corinthians', 'Flamengo',
                 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
                 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Ciuabá',
                 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
while True:
    print('---------Menu de Opções--------\n[1]Mostar G5\n[2]Mostrar Z4'
          '\n[3]Mostrar times em ordem alfabética\n[4]Pesquise uma dente as 20 posições e descubra qual time ficou nela')
    print('---' * 10)
    r = int(input('Qual sua escolha? [Digite 0 para parar] '))
    print('---' * 10)
    sleep(2)
    if r == 1:
        print(classificacao[:5])
    if r == 2:
        print(classificacao[16:])
    if r == 3:
        print(sorted(classificacao))
    if r == 4:
        escolha = 0
        while True:
            escolha = int(input('Qual posição deseja descobrir? '))
            if escolha > 0 and escolha <= 20:
                break
        print(f'O {classificacao[escolha - 1]}, ficou em {escolha}º')
    if r > 4:
        print('ESCOLHA INVÁLIDA')
    if r == 0:
        break
print('FIM DO PROGRAMA')






