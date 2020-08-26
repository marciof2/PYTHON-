def contagem(inicio, fim, passo):
    passo= abs(passo)
    fim+=1
    if passo ==0:
        passo=1  
    if inicio < fim:
        for c in range(inicio, fim, passo):
            print(c, end=' ')
        print('FIM')
        print()
        print('-'*30)
    else:
        for c in range(inicio, fim-1, -passo):
            print(c, end=' ')
        print('FIM')
        print()
        print('-'*30)


print('CONTAGEM DE 1 A 10 DE 1 EM 1:')
print('-'*30)
for c in range(1, 11):
    print(c, end=' ')
print('FIM')
print()
print('CONTAGEM DE 10 A 0 DE 2 EM 2:')
print('-'*30)
for c in range(10, -1, -2):
    print(c, end=' ')
print('FIM')
print()
print('Agora é sua vez de personalizar a sua contagem')
contagem(inicio= int(input('INICIO: ')), fim=int(input('FIM: ')), passo=int(input('PASSO: ')))