#código para calcular a aprovação de emprestimo com condição de o valor da parcela NÃO ser maior que 30% do salário.
valor_casa= float(input('Digite o valor da casa: '))
salario= float(input('Digite seu salário: '))
tempo= int(input('Digite o prazo para pagamento [ANOS]: '))
valor_prestaçao= valor_casa/tempo
porcentagem= salario*30/100
print('Em {} anos parcela terá o valor de {}.'.format(tempo, valor_prestaçao))
if valor_prestaçao > porcentagem:
    print('Infelizmente não podemos aprovar esse valor de empréstimo.')
else:
    print('PARABENS!! Seu empréstimo foi pré-aprovado !!')