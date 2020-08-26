'''Faça um programa que jogue par ou ímpar com o computador. O jogo 
só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
que ele conquistou no final do jogo'''
from random import randint
soma= v=0
div= 0
while True:
    comp= randint(0,10)
    jog=int(input('Escolha um número: '))
    pi=str(input(' PAR ou IMPAR: [P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        pi=str(input(' PAR ou IMPAR: [P/I] ')).strip().upper()[0]
    print('--' *20)
    soma=jog+comp
    div= soma % 2
    if div==0:
        print(f'O Computador jogou {comp} e você jogou {jog}. {soma} é PAR')
        print('--' *20)
        if pi =='P':
            print('Você venceu !')
            print('Vamos jogar de novo .. ')
            v+=1
        if pi == 'I':
            break
    if div != 0:
        print(f'O Computador jogou {comp} e você jogou {jog}. {soma} é IMPAR')
        print('--' *20)
        if pi =='I':
            print('Você venceu !')
            print('Vamos jogar de novo .. ')
            v+=1
        if pi == 'P':
            break
print(f'GAME OVER ! Você venceu {v} vezes.')
