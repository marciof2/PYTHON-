from datetime import date
ano_nasc= int(input('Ano de nascimento: '))
ano_atual= int(date.today().year)
idade= ano_atual - ano_nasc
if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR.'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e está na categoria SÊNIOR.'.format(idade))
else:
    print('Voce tem {} e anos está na categoria MASTER.'.format(idade))