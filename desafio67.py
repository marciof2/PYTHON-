c=1 #contador de 1 a 11 para mult o valor de N
t=0 #valor da mult de n por C
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1,11):
        t= c * n
        print(f'{n:2} x {c:2} = {t:2}')
        c+=c
    print('-'*30)
print('Programa finalizado')