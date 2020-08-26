n= int(input('Primeira Medida: '))
n2= int(input('Segunda Medida: '))
n3= int(input('Terceira Medida: '))
print('\n')
if n < n2 + n3 and n2 < n3 + n and n3< n + n2:
    print('É um TRIANGULO !!')
    if n==n2==n3:
        print('Classificado como EQUILÁTERO.')
    elif n != n2 and n!= n3 and n2!=n3:
        print('Classificado como ESCALENO.')
    elif n == n2 and n!= n3 or n2 == n3 and n2!=n or n3==n and n3!=n2:
        print('Classificado como ISÓSCELES.')
else:
    print('NÃO é um triangulo.')
print('\n')