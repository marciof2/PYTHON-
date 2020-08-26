lista= []
posimaior=[]
posimenor=[]
for c in range(0,5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
for pos, c in enumerate(lista):    
    if max(lista) == c:
        posimaior.append(pos)
    if min(lista) == c:
        posimenor.append(pos)
print('-='*30)
print(f'O maior valor encontrado na lista é {max(lista)} e está nas posições: {posimaior}')
print(f'O menor valor é {min(lista)} e foi encontrado nas posições:  {posimenor}')
