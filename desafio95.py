jogador= {}
dados= []
g= []
soma=0
while True:
    jogador['nome']= str(input('Nome do jogador: '))
    j= int(input(f'Quantos jogos {jogador["nome"]} jogou: '))
    if j == 0:
        g.append(0)
    for c in range(0,j):
        n =int(input(f'Gols na partida {c}: '))
        g.append(n)
        soma+=n
    print(g)  
    jogador['gols']= g[:]
    g.clear()
    jogador['soma']= soma
    soma=0
    dados.append(jogador.copy())
    while True:
        r= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<15}{"GOLS":<20}{"TOTAL":<10}')
for c in range(0, len(dados)):
    print(f'{c:<4}{dados[c]["nome"]:<20}{str(dados[c]["gols"]):<15}{dados[c]["soma"]:<10}')
print('-'*60)
while True:
    n= int(input('Deseja ver os detalhes de qual jogador? [999 PARA SAIR] '))
    if n== 999:
        break
    if n >= len(dados):
        print('JOGADOR INVÁLIDO, TENTE NOVAMENTE')
    else:
        print(f'-----DADOS DE {dados[n]["nome"]}:')
        for c in range(0,len(dados[n]['gols'])):
            print(f'Na partida {c+1} marcou {dados[n]["gols"][c]} gols.')
        print('-='*15)
print('ENCERRANDO ...')