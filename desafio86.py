linha=[]
coluna=[]
for c in range(0,3):
    for l in range(0, 3):
        n= int(input(f'Digite um valor para [{c}, {l}]: '))
        linha.append(n)
    coluna.append(linha[:])
    linha.clear()
for c in range(0,3):
    for l in range(0,3):
        print(f'[ {coluna[c][l]} ] ' , end=' ')
    print('\n')
