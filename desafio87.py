linha=[]
coluna=[]
soma= s_par= 0
maior=0
for c in range(0,3):
    for l in range(0,3):
        n= int(input(f'Digite o valor para [{c}, {l}]: '))
        linha.append(n)
    coluna.append(linha[:])
    linha.clear()
for c in range(0,3):
    for l in range(0,3):
        print(f'[ {coluna[c][l]} ] ', end=" ")
        if coluna[c][l] % 2 ==0:
            s_par+= coluna[c][l]
        if l ==1:
            maior= max(coluna[l])
    print('\n')
    soma+= coluna[c][-1]
print(f'A soma dos números pares é {s_par}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior valor da segunda coluna é {maior}')