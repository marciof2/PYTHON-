l=[[],[]]
n=[]
for c in range(1,8):
    n=int(input(f'Digite o {c}° valor: '))
    if n %2==0:
        l[0].append(n)
    elif n %2 ==1 :
        l[1].append(n)
print('-='*30)
l[0].sort()
print(f'Os números pares são : {l[0]}.')
l[1].sort()
print(f'Os números ímpares são: {l[1]}.')