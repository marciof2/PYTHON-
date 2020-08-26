s = 0 #soma dos números 
c= 0 #quantidade de números digitados
while True:
    n=int(input('Digite um valor: '))
    if n == 999: #caso digitar 999 o programa para antes de fazer a soma(IMPORTANTE: colocar essa condição antes de fazer a soma)
        break
    s+=n
    c+=1
print(f'A soma dos {c} valores é {s}.')
