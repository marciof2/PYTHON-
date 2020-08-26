n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m= (n1+n2)/2
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, m))
if m<6:
    print('VOCÊ ESTÁ REPROVADOOOOOOOO!!!!!!!!!!!')
if m>6:
    print('VOCÊ ESTÁ APROVADO!! PARABÉNS !!!')
if m ==6:
    print('VOCÊ ESTÁ APROVADO!! PARABÉNS !!!')
        