nome = str(input('Escreva se nome completo: ')).strip()
print('Seu nome escrito apenas em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome escrito apenas em letras minúsculas é {}'.format(nome.lower()))
print('Ele possui {} letras ao todo'.format(len(nome) - nome.count(' ')))
##print(len(nome),count))
print('Seu primro nome possui {} letras'.format(nome.find(' ')))




