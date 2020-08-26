jogador={}
jogador['nome']= str(input('Nome do jogador: '))
g= int(input('Quantas partidas foram jogadas: '))
gols=[]
soma= n =0
for c in range(0,g):
    n= int(input(f'Quantos gols na partida {c}: '))
    gols.append(n)
    soma+=n
jogador['gols'] = gols[:]
jogador['total_gols']= soma
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v} ')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {g} partidas.')
for c in range(0,g):
    print(f'Na partida {c}, fez {jogador["gols"][c]} gols ')
