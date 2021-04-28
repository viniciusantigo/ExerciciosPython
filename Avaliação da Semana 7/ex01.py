'''Faça um programa que, para cada um dos 30 alunos de uma turma, leia o nome e as três notas do aluno, 
mostre o nome, a média final e o conceito, sabendo-se que:

A média final é calculada pela média aritmética das 3 notas;
O conceito é determinado de com base na tabela abaixo:
Determine e mostre também:

A quantidade de alunos com conceito A;
A quantidade de alunos com conceito B;
A quantidade de alunos com conceito C;
A quantidade total de alunos da turma.'''

conta = 0
contb = 0
contc = 0
for i in range(3):
	nome = input('Informe o nome do(a) aluno(a): ')
	n1 = float(input('Primeira nota: '))
	n2 = float(input('Segunda nota: '))
	n3 = float(input('Terceira nota: '))
	media = (n1 + n2 + n3) / 3
	if media >= 7:
		conceito = 'A'
		conta += 1
	elif media >= 4:
		conceito = 'B'
		contb += 1
	else: 
		conceito = 'C'
		contc += 1
	print(f'Nome: {nome}')
	print(f'Média final: {media:.1f}')
	print(f'Conceito: {conceito}')
	print('--' * 20)
print(f'Alunos com conceito A: {conta}')
print(f'Alunos com conceito B: {contb}')
print(f'Alunos com conceito C: {contc}')
print(f'Quantidade de alunos na turma: {i + 1}')
