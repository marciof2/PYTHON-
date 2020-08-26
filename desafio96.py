def area(larg, comp):
    a= larg*comp
    print(f'O comprimento de um terreno {larg}x{comp} é igual a {a}m².')


print('Controle de Terrenos')
print('-'*20)
l=float(input('LARGURA:  '))
c=float(input('COMPRIMENTO: '))
area(l, c)
