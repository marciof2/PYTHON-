numeros=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True: 
      n=int(input('Digite um número entre 0 e 20: '))
      if n >= 0 and n <=20:
        break
    print(f'Você digitou o número {numeros[n]}')
    while True:
      c= str(input('Quer continuar ? [S/N]')).upper().strip()
      if c in 'SN':
        break
    if c == 'N':
      break
print('PROGRAMA FINALIZADO')