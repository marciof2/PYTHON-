alunos=[]
nomes=[]
notas=[]
print('-'*30)
print(f'{"ESCOLA MEC2 PARA INDIOTAS":^30}')
print('-'*30)
while True:
    nomes.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nomes.append(notas[:])
    notas.clear()
    alunos.append(nomes[:])
    nomes.clear()
    r= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r= str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-'*30)
print(F'{"NOTAS":^30}')
print('-'*30)
print(f'{"N°":2} {"Nome":10} {"Média"}')
for c in range(0, len(alunos)):
    print(f'{c:<2}', end=" ")
    print(f'{alunos[c][0]:10} {(alunos[c][1][0]+alunos[c][1][1])/2:.1f}')
print('-'*30)
while True:
    n= int(input('Deseja ver a nota de qual aluno? [ 999 PARA PARAR ] :  '))
    if n == 999:
        break
    if n <= len(alunos)-1:
        print(f'As notas de {alunos[n][0]} foram: {alunos[n][1][0]} e {alunos[n][1][1]}')
print('VOLTE SEMPRE !')
