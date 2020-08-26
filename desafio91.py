from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador 1': randint(0,6),
       'jogador 2': randint(0,6),
       'jogador 3': randint(0,6),
       'jogador 4': randint(0,6)}
rank= {}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
rank= sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('   == RANKING DO JOGADORES ==')
for i, c in enumerate(rank):
    print(f'{i+1}° lugar: {c[0]} com {c[1]}')
    sleep(1)
