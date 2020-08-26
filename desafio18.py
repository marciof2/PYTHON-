from math import cos, sin, tan, radians
n1= int(input('Digite um número em os graus: '))
seno= sin(radians(n1))
coss= cos(radians(n1))
tang= tan(radians(n1))
print('Você digitou {:.2f} \nO cosseno é igual a: {:.2f}\nO seno é igual a: {:.2f}\nA tangente é igual a: {:.2f}'.format(n1, coss, seno, tang))
