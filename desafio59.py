from time import sleep
import os
resp=0
n1= int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
while resp != '5':
    resp=str(input('''OPÇÕES:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]DIGITAR NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA
    Escolha uma das opções acima: '''))
    if resp == '1': #PARTE SOMA DO MENU
        print('SOMANDO OS NÚMEROS... AGUARDE')
        sleep(1)
        print(f'A soma dos números é {n1+n2}.')
    elif resp == '2': #PARTE MULT DO MENU
        print('MULTIPLICANDO OS NÚMEROS.. AGUARDE')
        sleep(1)
        print(f'O produto dos valores digitados é {n1*n2}.')
    elif resp == '3': #PARTE MAIOR NÚMERO DO MENU 
        print('CALCULANDO O MAIOR NÚMERO... AGUARDE')
        sleep(1)
        if n1 > n2:
            print(f'O maior número é {n1}.')
        elif n1 < n2:
            print(f'O maior número é {n2}.')
        elif n2==n1:
            print('Os números são iguais.')
    elif resp == '4': #PARTE DE ESCOLHER NOVOS NÚMEROS
        print('ESCOLHA NOVOS NÚMEROS')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))
    elif resp not in '54321':
        print('OPÇÃO INVÁLIDA !')
    sleep(2)
print('Você finalizou o programa')
