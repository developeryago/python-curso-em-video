from datetime import date #Importação para verificar o ano configurado na máquina
ano = int(input('Digite o ano que deseja pesqusar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Ordem para puxar o ano configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Uma estrutura if não anula a outra
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))
