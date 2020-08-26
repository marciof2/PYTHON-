from datetime import date
ano_atual=  date.today().year
maior=0
menor=0
for c in range(1,8):
    ano= int(input('Digite o ano a {}° pessoa nasceu: '))
    if ano_atual - ano >= 21:
        maior+=1
    else:
        menor+=1 
print('dos 7 calculados temos {} maiores de idade e {} menores de idade.'.format(maior, menor))