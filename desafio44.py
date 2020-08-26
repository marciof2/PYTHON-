valor= float(input('Qual o valor do produto?'))
pag= int(input('''Qual será a forma de pagamento?
            [1] DINHEIRO/CHEQUE: 10% DE DESCONTO
            [2] À VISTA NO CARTÃO: 5% DE DESCONTO
            [3] EM ATÉ 2X NO CARTÃO: SEM DESCONTO
            [4] 3X OU MAIS NO CARTÃO: 20% DE JUROS
            '''))
if pag== 1:
    valor= valor - (valor*10)/100
    print('Vpcê recebeu 10% de desconto, o valor final do produto será R${:.2f}'.format(valor))
elif pag == 2:
    valor= valor - (valor*5)/100
    print('Você recebeu 5% de desconto, o valor final do produto será R${:.2f}'.format(valor))
elif pag == 3:
    print('Você escolheu uma forma de pagamento sem descontos.')
else:
    valor= valor + (valor*20)/100
    print('Em caso de parcelamento em 3X ou mais, será acrescentado 20% de juros, o valor do produto será R${:.2f}'.format(valor))
print('\n')