pri= int(input('Primeiro termo: '))
razao= int(input('Razão: '))
c= 1
while c < 11:
    print(pri, end='-> ')
    pri+=razao
    c+=1
print('ACABOU')
