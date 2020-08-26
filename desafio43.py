
peso= float(input('Qual seu peso? [KG] '))
alt= float(input('Qual a sua altura? '))
imc= peso/(alt**2)
print('\n')
print('-'*25)
print('RESULTADO')
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
print('\n')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc< 25:
    print('PESO IDEAL')
elif 25<= imc<30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MÓRBIDA')
print('\n')
