from time import sleep
print('\033[37m-=\033[m' * 45)
print('Vamos calcular seu Índice de Massa Corporal! Para isso preciso que me dê duas informações')
print('\033[37m-=\033[m' * 45)
p = float(input('Qual é o seu peso?(Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC deu {:.2f} e você está ABAIXO DO PESO!'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('Seu IMC deu {:.2f} e você está no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc <= 29.9:
    print('Seu IMC deu {:.2f} e você está com SOBREPESO!'.format(imc))
elif imc >= 30 and imc <= 39.9:
    print('Seu IMC deu {:.2f} e você está OBESO!'.format(imc))
elif imc > 40:
    print('Procure um médico urgentemente, você está com OBESIDADE MÓRBIDA!'.format(imc))

