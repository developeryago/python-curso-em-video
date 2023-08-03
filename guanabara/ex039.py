from datetime import  date
ano = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - ano
if idade == 18:
    print('Você atingiu {} anos e precisará prestar alistamento obrigatório IMEDIATAMENTE!'.format(idade))
elif idade < 18:
    tempo = 18 - idade
    print('Você ainda não atingiu os 18 anos, mas daqui á {} anos precisará prestar alistamento obrigatório!'.format(tempo))
    print('Seu alistamento será em {}'.format(date.today().year + tempo))
else:
    tempo = idade - 18
    print('Já se passaram {} anos desde que fez 18 anos'.format(tempo))
    r = str(input('Você deveria ter se alistado em {}, confirma ter feito isso? '.format(date.today().year - tempo))).lower().strip()
    if r == 'sim' or r == 'claro' or r == 'com certeza' or r == 'obvio' or r == 'yes':
        print('Então você pode seguir com sua vida normalmente.')
    else:
        print('Você está em PENDÊNCIA com o governo, busque prestar contas imediatamente!')

