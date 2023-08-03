s = str(input('Qual seu sexo? [M]/[F] ')).strip().upper()[0]
while s not in 'MF': #Atenção ao usar 'not in' (não for)  #Mesmo dentro das aspas, M e F são lidos separadamente
    s = str(input('Dados inválidos, digite novamente: [M]/[F]')).strip().upper()[0] # O número zero faz o fatiamento da primeira letra da str
print('Sexo {} registrado com sucesso!'.format(s))


'''while s != 'M' and s != 'F' #Tentativa falhada de fazer o programa 
    s = str(input('Qual seu sexo? [M]/[F] ')).strip().upper()[0]
    if s != 'M' or s != 'F':
        print('Dados inválidos! Tente novamente.')
print('----FIM-----')'''
