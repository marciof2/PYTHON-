n= int(input('Primeira Medida: '))
n2= int(input('Segunda Medida: '))
n3= int(input('Terceira Medida: '))
print('\n')

if n < n2 + n3 and n2 < n3 + n and n3< n + n2:
    print('É um TRIANGULO !!')
else:
    print('NÃO é um triangulo.')
print('\n')
