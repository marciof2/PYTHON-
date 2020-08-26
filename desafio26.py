nome=str(input('Digite um nome: ')).upper().strip()
print('Letras A encontradas: {}'.format(nome.count('A')))
print('Primeira letra A encontrada: {}'.format(nome.find('A')+1))
print('Última letra A encontrada: {}'.format(nome.rfind('A')+1))