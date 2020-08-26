from random import randint
sorteados= (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os números sorteados foram ', end='')
for n in sorteados:
    print(n, end=' ')
print(f'\nO maior número é {max(sorteados)}')
print(f'O menor número é {min(sorteados)}.')