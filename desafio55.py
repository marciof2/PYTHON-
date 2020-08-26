menor= 0
maior = 0
for c in range(0,5):
    peso= float(input('Digite o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:    
        if peso > maior:
            maior= peso
        elif peso < menor:
            menor = peso
print('MAIOR: {}Kg'.format(maior))
print('MENOR: {}Kg'.format(menor))