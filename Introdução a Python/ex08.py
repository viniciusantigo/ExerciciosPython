'''8. Faça um programa que leia o nome de um aluno e as notas das três provas que ele
obteve no semestre. No final informar o nome do aluno e a sua média (aritmética).'''

nome = input('Informe seu nome: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3
print('Aluno(a):', nome)
print(f'Média: {media:.1f}')
