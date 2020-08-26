maior18=0 #recebe menores de 18 anos
homens=0 #recebe o total de homens
mulher20=0 #recebe mulheres abaixo de 20 anos
p=1 #print da 1° linha
while True:
    print(f'------------- {p}° PESSOA ------------- ')
    idade=int(input('Digite a idade: '))
    sexo= str(input('Digite o sexo: [M/F] ')).strip().upper()
    while sexo not in 'MF': #repetição para sexo diferente de M e F
        sexo= str(input('Digite o sexo: [M/F] ')).strip().upper()
    print('-'*30)
    c= str(input('Deseja continuar? [S/N] ')).strip().upper()
    while c not in 'SN': #repetição para reposta diferente de S e N
        c= str(input('Deseja continuar? [S/N] ')).strip().upper()   
    if idade >= 18: #calculando pessoas maiores de 18 anos
        maior18+=1
    if sexo == 'M': #calcula homens no total 
        homens+=1
    if sexo == 'F' and idade < 20: #calcula mulheres abaixo de 20 anos
        mulher20+=1
    if c == 'N': #condição de parada, caso c seja NÃO
        break
    p+=1
print(f'Das pessoas cadastradas {maior18} são maiores de 18 anos.')
print(f'Foram {homens} homens cadastrados. ')
print(f'E foram cadastradas {mulher20} mulheres abaixo dos 20 anos. ')
