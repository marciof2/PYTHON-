n= int(input('Digite um número INTEIRO: '))
print('''Escolha uma das opções:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
escolha= int(input('Sua escolha: '))
if escolha == 1:
    print('A conversão de {} para  BINÁRIO resulta em {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('A conversão de {} para OCTAL resulta em {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('A conversão de {} para HEXADECIMAL resulta em {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')