soma= 0
cont=0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont+=1
        soma += c
        print(c)
print('A soma dos {} números DIVISÍVEIS por 3 é igual a {}.'.format(cont, soma))
