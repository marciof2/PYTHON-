from random import randint
from time import sleep
n= (randint(0,2))
itens= (['Pedra', 'Papel', 'Tesoura'])
jpc= ((itens[n]))
print(jpc)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
j= int(input('Qual é a sua jogada? '))
if j > 2:
  print('JOGADA INVALIDA')
else:
  print('JO')
  sleep(1)
  print('KEN')
  sleep(1)
  print('PO')
  sleep(1)
  print('O COMPUTADOR jogou {} e VOCÊ jogou {}...'.format(itens[n], itens[j]))
  sleep(1)
  if n== j:
    print('EMPATE !')
  elif n == 0: #PEDRA
    if j == 1:
      print('VOCÊ VENCEU !!!')
    elif j == 2:
      print('VOCÊ PERDEU!!')
    else:
      print('JOGADA INVÁLIDA')
  elif n == 1: #PAPEL
    if j == 0:
      print('VOCÊ PERDEU!!')
    elif j == 2:
      print('VOCÊ VENCEU !!!')
    else:
      print('JOGADA INVÁLIDA')
  elif n== 2: #TESOURA
    if j == 0:
      print("VOCÊ VENCEU !!")
    elif j == 1:
      print('VOCÊ PERDEU !!')
    else:
      print('JOGADA INVÁLIDA')
