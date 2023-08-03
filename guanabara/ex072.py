cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0  e 20: '))
    if n >= 0 and n <= 20: #Poderia utilizar a sintaxe: 0 <= n <= 20
        print(f'Você digitou o número {cont[n]}')
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if r == 'N':
            break
    else:
        print('ESCOLHA INVÁLIDA!', end= ' ')
print('FIM')


