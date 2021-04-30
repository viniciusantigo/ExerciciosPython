'''7. Escreva um programa que leia 4 notas e calcule a média obtida, desprezando a nota mais baixa.
O programa deverá determinar o conceito do aluno na disciplina, de acordo com a tabela
seguinte:

MÉDIA CONCEITO
≥ 9,0 A
≥ 8,0 e < 9,0 B
≥ 6,0 e < 8,0 C
≥ 4,0 e < 6,0 D
< 4,0 E

Ao final, mostrar a média, o conceito correspondente e a mensagem APROVADO (se o conceito
for A, B ou C) ou REPROVADO (se o conceito for D ou E).'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4

print(f'Média: {media:.1f}')

if media >= 9:
    print('Conceito A')
    print('Aprovado!')
elif media >= 8:
    print('Conceito B')
    print('Aprovado!')
elif media >= 6:
    print('Conceito C')
    print('Aprovado!')
elif media >= 4:
    print('Conceito D')
    print('Reprovado!')
elif media < 4:
    print('Conceito E')
    print('Reprovado!')
else:
    print('Média inválida')