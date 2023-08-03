from math import sin,cos,tan,radians
ang = float(input('Digite um ângulo: '))
print('Para o ângulo de {} seu SENO é {:.2f}'.format(ang,sin(radians(ang))))
print('Seu COSSENO é {:.2f}'.format(cos(radians(ang))))
print('Sua TANGENTE é {:.2f}'.format(tan(radians(ang))))


