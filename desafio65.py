resp= 'S'
soma=0
menor = maior =0
q=0
while resp in 'Ss':
    n=int(input('Digite um número: '))
    resp= str(input('Deseja continuar? [S/N] '))  
    q+=1
    soma+=n  
    if q== 1:
        maior=n
        menor=n
    else:
        if n < menor:
            menor=n
        if n > maior:
            maior=n
print(f'A média dos números digitados é {soma/q}.')
print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
