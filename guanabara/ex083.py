expr = str(input('Digite a expressão: '))
contparenteses = []
for c in expr:
    if c == '(':
        contparenteses.append('(')
    elif c == ')':
        if len(contparenteses) > 0:
            contparenteses.pop()
        else:
            contparenteses.append(')')
            break
if len(contparenteses) == 0:
    print('Sua expressão está VÁLIDA!')
else:
    print('Sua expressão está INVÁLIDA!')
