total =0 #recebe o valor total dos produtos
mais=0 #recebe quantidade de produtos acima de 1000 reais
q=0 #recebe a quantidade de produtos cadastrados
while True:
    nome=str(input('Nome do Produto: ')).strip()
    preço= float(input('Preço: R$'))
    print('-'*30)
    c= str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while c not in 'NS':
        c= str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    total+=preço
    q+=1
    if q == 1 or preço < barato:
            barato = preço
            nome_barato=nome
    if preço > 1000:
        mais+= 1
    if c == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto foi de {total:.2f}')
print(f'{mais} produtos passam de R$1000.00.')
print(f'O produto mais barato foi {nome_barato} e custou {barato:.2f}')