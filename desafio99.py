def maior(*num):
    maior=0
    tam= len(num)
    for pos, c in enumerate(num):
        if pos == 0:
            maior = c
        else:
            if c > maior:
                maior= c
    if tam == 0:
        print('Não foi digitado nenhum número. ')
    else:
        print('Analisando os valores passados...')
        print('Foram informados ', end=' ')
        for c in num:
            print(c, end=', ')
        print(f'somando {len(num)} números ao todo')
        print(f'O maior número informado foi {maior}.')
        print('-='*40)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()