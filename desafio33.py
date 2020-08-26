n= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
n3= int(input('Digite o terceiro número: '))
if n > n2 and n> n3:
    print('O maior número é {}'.format(n))
if n2 > n3 and n2 > n:
    print('O maior número é {}'.format(n2))
if n3 > n2 and n3> n:
    print('O maior número é {}'.format(n3))
if n < n2 and n< n3:
    print('O menor número é {}'.format(n))
if n2 < n and n2 < n3:
    print('O menor número é {}'.format(n2))
if n3 < n and n3 < n2:
    print('O menos número é {}'.format(n3))
    