'''6. Recomendam-se estudantes para bolsas de estudo em função de seu
desempenho. A natureza das recomendações é baseada na seguinte tabela:
Escreva um programa que leia o nome e o conceito de um estudante e
exiba o nome do estudante e sua respectiva recomendação.'''

nome = input('Informe o nome do(a) estudante: ')
conceito = input('Informe o Conceito do(a) estudante: ').upper()

print(f'Aluno: {nome}')
if conceito == 'A':
 print('Recomendação: Fortemente recomendado.')
elif conceito == 'B' or conceito == 'C':
 print('Recomendação: Recomendado.')
elif conceito == 'D':
 print('Recomendação: Não recomendado.')
else:
 print('Conceito não aceito. Informe um conceito válido.')
