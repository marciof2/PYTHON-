from datetime import date
ano_nasc= int(input('Ano de nascimento: '))
ano_atual= date.today().year
idade= ano_atual - ano_nasc
if idade < 18:
    print('Você tem {} anos.'.format(idade))
    print('Ainda é muito cedo para se alistar, espere {} ano/s.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(18-idade+ano_atual))
elif idade == 18:
    print('Você tem {} anos.'.format(idade))
    print('Está na hora de se alistar soldado !!.')
else:
    print('Você tem {} anos.'.format(idade))
    print('Já passou {} ano/s do prazo final para alistamento.'.format(idade-18)) 
    print('Seu alistamento deveria ter sido feito em {}.'.format(ano_nasc+18))