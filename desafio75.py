n1= int(input('Digite um valor: '))
n2=int(input('Digite um valor: '))
n3=int(input('Digite um valor: '))
n4=int(input('Digite um valor: '))
t= (n1, n2 , n3 ,n4)
print(f'Os valores digitadors foram {t}')
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O número 3 apareceu na {t.index(3)+1}° posição. ')
else:
    print('Não tem números 3.')
par=0
print('Os valores pares digitados foram: ', end=' ')
for c in t:
    if c %2==0:
        par=c
        print(c, end=' ')
