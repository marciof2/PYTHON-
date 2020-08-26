from random import randint
lista= []
pares=[]
def sorteio():
    for c in range(0, 5):
        lista.append(randint(0,10))
    print(f'Valores sorteador: {lista}')


def soma():
    s=0
    for c in lista:
        if c %2==0:
            s+=c
            pares.append(c)
    print(f'Somando os valores pares {pares}, temos {s} ')


sorteio()
soma()