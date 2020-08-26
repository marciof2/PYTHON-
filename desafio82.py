l=[]
l_par=[]
l_impar=[]
while True:
    n= int(input('Digite um valor: '))
    l.append(n)
    r= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for c in l:
    if c %2==0:
        l_par.append(c)
    elif c %2==1:
        l_impar.append(c)
print('-='*30)
print(f'Os números digitados foram : {l}')    
print(f'Desses números os pares são: {l_par}')
print(f'E os ímpares são: {l_impar}')
