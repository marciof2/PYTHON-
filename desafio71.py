while True:
    print('-='*30)
    saque= int(input('Valor do saque: R$'))
    n50= int(saque /50)
    resto= saque - n50 *50
    if n50 > 0:
        print(f'Notas de R$50: {n50:2}')
    if resto != 0:
        if resto==0:
            break
        else:
            n20= int(resto / 20)
            resto= resto - n20 * 20
            if n20 > 0:
                print(f'Notas de R$20: {n20:2}')
            else:
                n10= int(resto / 10)
                resto = resto - n10 * 10
                if n10 > 0:
                    print(f'Notas de R$10: {n10:2}')
                else:
                    n1= resto * 1
                    if n1 > 0:
                        print(f'Notas de R$1: {n1:2}')
    break
print('-='*30)  
print('OBRIGADO E VOLTE SEMPRE ')                   
