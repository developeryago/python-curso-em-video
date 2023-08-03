l = float(input('Qual a largura da parede: '))
a = float(input('Qual a altura da parede: '))
print('Sua parede tem dimensão de {}x{} e sua área é de {:.2f}m²'.format(l,a,l*a))
t = (l*a)/2
print('Para pintar sua parede você precisará de {}l de tinta'.format(t))

