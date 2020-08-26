n= float(input('Digite um valor: '))
cen= n*100
mili= n*1000
km= n/1000
dec= n/10
print('\nVocê que converter {} metros, certo ? \nOk, vamos lá!!'.format(n))
print('\nPara {} metros temos: \n{} centímetros \n{} milímetros \n{} quilômetros \n{} hectômetros \n{} decametros.'.format(n, cen, mili, km, km, dec))