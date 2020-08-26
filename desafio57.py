sexo=''
while sexo!= 'M' and sexo!= 'F':
  sexo= str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
  if sexo != 'M' and sexo != 'F':
    print('TENTE NOVAMENTE ! SEXO INVÁLIDO !')
  else: 
    print(f'Sexo {sexo} registrado com sucesso !')