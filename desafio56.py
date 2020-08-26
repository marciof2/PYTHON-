menor_20=0
media= 0
mais_velho=0
velho=0
somaidade= 0
for p in range(0,4):
    nome= str(input('Nome da pessoa: ')).strip()
    idade= int(input('Idade da pessoa: '))
    sexo= str(input('Sexo da pessoa [F/M]: ')).strip()
    somaidade= idade + somaidade
    if p == 1 and sexo in 'Mm':
        mais_velho= idade
        nome_velho= nome
    if sexo in 'mM' and idade > mais_velho:
        mais_velho= idade
        nome_velho= nome
    if idade < 20 and sexo in 'Ff':
        menor_20+= 1
media= somaidade/4
print('A média de idade é de {} anos.'.format(media))
print('O homem mais velho é {} com {} anos.'.format(nome_velho, mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menor_20))
        
 