from random import randint
from time import sleep
jogos=[]
print('-='*30)
print(f'{"JOGO NA MEGASENA":^60}')
print('-='*30)
n= int(input('Quantos jogos deseja fazer ? '))
for c in range(1, n+1):
    while len(jogos) < 6:
        e = randint(0,60)
        if e not in jogos:
            jogos.append(e)
        else:
            if e in jogos:
                jogos.remove(e)
                e = randint(0,60)
                jogos.append(e)
    jogos.sort()
    print(f'Jogo {c}: {jogos}')
    sleep(1)
    jogos.clear()