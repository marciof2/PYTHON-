n=0
q=0
soma=0
while n != 999:
    n=int(input('Digite um número: '))
    if n != 999:
        q+=1
        soma+=n
print(f'Você digitou {q} números.')
print(f'A soma dos números é igual a {soma}')
print('FIM')
