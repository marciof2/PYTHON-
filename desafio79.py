lista= []
while True:
    n= int(input('Digite um valor: '))
    valores.append(n)
    if n not in lista:
        print('Adicionado com sucesso ')
        lista.append(n)
    else:
        print('Valor Duplicado, Não vou adicionar ')
    r= str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r= str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
    if 'N' in r:
        break
print('-='*30)
lista.sort()
print(f'Esses foram os números que sobraram depois de retirar os repetidos: {lista}').upper()
print('FIM DO PROGRAMA')
    