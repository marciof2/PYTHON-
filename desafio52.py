n= int(input('Digite um número: '))
total= 0 #numero de vezes que o N foi dividido e deu 0
for c in range(1, n+1):
    if n % c==0:
        total+= 1
if total == 2:
    print('{} É PRIMO.'.format(n))
else: 
    print('NÃO é primo')
