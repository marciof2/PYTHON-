num= int(input('Calcular seu fatorial: '))
c = num
f=1
while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end= '')
    else:
        print(' = ', end='')
    f *= c
    c-=1
print(f)
