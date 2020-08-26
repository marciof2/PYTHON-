salario= float(input('Qual o seu salário atual? '))

if salario <= 1250:
    print('Seu novo salário é R${}'.format(salario + (salario/100)*15))
else:
    print('Seu novo salário é R${}'.format(salario + (salario/100)*10))