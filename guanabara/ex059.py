from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
escolha = maior = 0
while escolha != 5:
    sleep(2)
    print('-----MENU DE OPÇÕES-----')
    print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR VALOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA')
    escolha = int(input('Qual é a sua opção? '))
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2,n1 + n2))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor digitado foi {}'.format(maior))
    elif escolha == 4:
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente.')
print('-=-' * 5, 'FIM DO PROGRAMA', '-=-' * 5)
