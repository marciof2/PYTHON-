l=('Fone', 98,'Mochila', 56, 'Luminária', 34, 'Caixa de Som', 85, 'Cadeira',
 650, 'Carregador', 30, 'Canetas', 16.30, 'Impressora', 865.99)
print('-='*20)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print('-='*20)
for item in range(0, len(l)):
    if item %2==0:
        print(f'{l[item]:.<30}',end='')
    else:
        print(f'R${l[item]:>7.2f}')
