n= input('Digite um número entre 0 e 9999: ')
if len(n)== 4:
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n '.format(n[0], n[1], n[2], n[3]))
else:
    if len(n)== 3:
        print('Unidade: {}\nDezena: {}\nCentena: {}\n'.format(n[0], n[1], n[2]))
    else:
        if len(n) == 2:
            print('Unidade: {}\nDezena: {}'.format(n[0], n[1]))
        else:
            print('Unidade: {}\n'.format(n[0]))

