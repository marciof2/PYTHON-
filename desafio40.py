print('-=-='*15)
n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
media= (n1+n2)/2
print('''SUAS NOTAS FORAM {:.1f} e {:.1f}
AGUARDE O CÁLCULO...'''.format(n1, n2))
print('-'*25)
print('Sua MÉDIA foi de {:.1f}.'.format(media))
if media < 5:
    print('Você está REPROVADO!')
elif media >= 5 and  media<= 7:
    print('Você está de RECUPERAÇÃO !')
else:
    print('PARABÉNS !! Você está APROVADO !!!')