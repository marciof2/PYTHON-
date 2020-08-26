pri= int(input('Primeiro termo: '))
razao= int(input('Razão: '))
c= 1
total=0
mais= 10
while mais != 0:
    total += mais
    while c <= total:
        print(pri, end=' ->')
        pri+=razao
        c+=1
    print('PAUSA')
    mais= int(input('Deseja mostrar mais quantos termos? '))
print('ACABOU')
print(f'O total de termos mostrados é {total}')