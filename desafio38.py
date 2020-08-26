n1 = int(input('Primeiro número: '))
n2= int(input('Segundo número: '))

if n1 > n2:
    print('{} é o maior valor.'.format(n1))
elif n2 > n1:
    print('{} é o maior valor.'.format(n2))
else:
    print('Os números são IGUAIS.')
