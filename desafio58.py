from random import randint
comp= randint(0,10)
jog= 11
cont= 0
while jog != comp:
  jog=int(input('FAÇA SUA JOGADA: '))
  cont+= 1
  if jog == comp :
    print('PARABÉNS! VOCÊ ACERTOU !!')
  else:
    if jog < comp:
      print('Um pouco mais')
    if jog > comp:
      print('Um pouco menos')
print('Você precisou de {} jogadas para vencer.'.format(cont))

