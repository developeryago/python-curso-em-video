n = int(input('Digite um número inteiro qualquer: '))
print('''Escollha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
escolha = int(input('Qual a sua escolha: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print('ESCOLHA INVÁLIDA!\nDigite um número entre 1 e 3')
