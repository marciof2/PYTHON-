from datetime import date
print(date.today().year)
dados={}
dados['nome']= str(input('Nome: '))
dados['idade']= date.today().year - (int(input('Ano de Nascimento: ')))
dados['ctps']= int(input('Carteira de trabalho: [DIGITE 0 CASO NAO TENHA] '))
if dados['ctps'] != 0:
    dados['contratação']= int(input('Ano de Contratação: '))
    dados['salario']= float(input('Salário: R$'))
    dados['aposentadoria']= 35 - (date.today().year - dados['contratação'] ) + dados['idade']
else: 
    print('Fim do Progama')
for k,v in dados.items():
    print(f'- {k} tem o valor {v}')