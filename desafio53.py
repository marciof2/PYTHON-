frase= str(input('Digite a frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))
palavras= frase.split()
junto= ''.join(palavras)
inverso= ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndomo!')
else:
    print('NÃO é um palíndromo')