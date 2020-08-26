aluno={}
aluno['nome']= str(input('Nome: '))
aluno['media']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] <= 4:
  aluno['situação'] = 'Reprovado'
elif aluno['media'] > 4 and aluno['media'] <= 7:
    aluno['situação']= 'Recuperação'
elif aluno['media'] > 7:
  aluno['situação']= 'Aprovado'
print('-='*15)
for k, c in aluno.items():
    print(f'- {k} é igual a {c}')