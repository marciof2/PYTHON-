lista=[]
mulheres=[]
acima_media=[]
dados={}
soma=media=0
while True:
    dados['nome']= str(input('Nome: '))
    dados['sexo']= str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        print('ERRO! Por favor digite M ou F')
        dados['sexo']= str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade']= int(input('Idade: '))
    soma+=dados['idade']
    lista.append(dados.copy())
    r= str(input('Deseja continuar? [S/N] ')).strip().upper()
    while r not in 'SN':
        r= str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r in 'N':
        break
print('-='*30)
media= soma / len(lista)
print(f'Foram cadastradas {len(lista)} pessoas. ')
print(f'A média de idade das {len(lista)} pessoas cadastradas é: {media:.2f}')
for c in lista: #CONTAGEM DAS MULHERES CADASTRADAS
    if c['sexo'] == 'F':
        mulheres.append(c['nome'])
if len(mulheres)==0:
    print('Nenhuma mulher cadastrada.')
else:
    print(f'Lista de mulheres: {mulheres}')
for c in lista: #PESSOAS ACIMA DA MÉDIA
    if c['idade'] > soma/len(lista):
        acima_media.append(c['nome'])
if len(acima_media) == 0:
    print('Ningúem está acima da média.')
else:
    print(f'Pessoas com idade acima da média: {acima_media} ')