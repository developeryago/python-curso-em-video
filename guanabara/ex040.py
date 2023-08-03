n1 = float(input('Qual foi sua nota no teste? '))
n2 = float(input('qual foi sua nota na prova? '))
media = (n1 + n2) / 2
if media < 5:
    print('Com as notas {:.1f} e {:.1f} você obteve média {:.1f} e foi \033[31mREPROVADO\033[m!'.format(n1,n2,media))
elif media > 5 and media < 6.9:
    print('Com as notas {:.1f} e {:.1f} você obteve média {:.1f} e está de \033[33mRECUPERAÇÃO\033[m!'.format(n1,n2,media))
else:
    print('Parabéns! \nCom as notas {} e {} você obteve média {} e foi \033[32mAPROVADO\033[m!'.format(n1, n2, media))



