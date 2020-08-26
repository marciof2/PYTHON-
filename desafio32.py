ano= int(input('Qual o ano deseja verificar? ')) 
if ano%4 ==0 or ano%400==0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))