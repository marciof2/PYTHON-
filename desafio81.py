lista=[]
n_digitados= cin=0
r= ''
while True:
    lista.append(int(input('Digite um valor: ')))
    r= str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while r not in 'SN':
        r= str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
print(f'Ao todo foram digitados {len(lista)} números. ')
lista.sort(reverse=True)
print(f'O lista em ordem DECRESCENTE é: {lista}')
if lista.count(5) >= 1:
    print(f'Foram encontrados {lista.count(5)} números 5 na lista ')
else:
    print('Não foram encontrados números 5 ')
