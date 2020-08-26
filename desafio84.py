l=[]
d=[]
menor= 0
maior=0
l_menor=[]
l_maior= []
while True:
    l.append(str(input('Nome: ')))
    l.append(float(input('Peso: ')))
    d.append(l[:])
    l.clear()
    r= str(input('Deseja continuar? [S/N] ')).strip()[0]
    while r not in 'SsNn':
      r= str(input('Deseja continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
for p, c in enumerate(d):
    if p ==0 :
        menor=c[1]
        l_menor.append(c[0])
        maior=c[1]
        l_maior.append(c[0])
    else:
        if c[1] == menor:
            l_menor.append(c[0])
        if c[1] < menor and menor not in l_menor:
            l_menor.clear()
            menor= c[1]
            l_menor.append(c[0])
        if c[1] == maior:
            l_maior.append(c[0])
        if c[1] > maior and c[1] not in l_maior:
            l_maior.clear()
            maior= c[1]
            l_maior.append(c[0])
print(f'Foram cadastradas {len(d)} pessoas')
print(f'O menor peso registrado foi de {l_menor} com {menor:.1f}KG')
print(f'E o maior peso é de {l_maior} com {maior:.1f}KG')
