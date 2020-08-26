n= float(input('DIGITE A ALTURA DA PAREDE: '))
n2= float(input('DIGITE A LARGURA DA PAREDE: '))
mtq= n*n2
tinta= mtq/2
print('Sua parede tem a dimensão de {:.2f}X{:.2f} e sua área é de {}m².'.format(n, n2, mtq))
print('Serão gastos {}l para pintar a parede.'.format(tinta))