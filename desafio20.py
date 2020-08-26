from random import sample

n1= str(input('Aluno 1: ')) 
n2= str(input('Aluno 2: ')) 
n3= str(input('Aluno 3: ')) 
n4= str(input('Aluno 4: ')) 
nomes= (n1, n2, n3, n4)
ran= tuple(sample(nomes, len(nomes)))
print(ran)
