'''6. Na primeira etapa de um concurso, o candidato tem que fazer duas provas. Dessas duas notas é
tirada a média do candidato. Caso essa média seja maior ou igual a 7.0, ele estará apto a fazer a
segunda etapa do concurso. Na segunda etapa, ele fará mais uma prova, onde deverá obter uma
nota maior ou igual a 8.0 para ser aprovado no concurso.
Escreva um programa que leia as notas da primeira etapa, calcule a média da primeira etapa, e
se o candidato for aprovado na primeira etapa, leia a nota dele na segunda etapa e diga se ele
foi aprovado ou não no concurso.'''

print('Primeira etapa!')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print('Você passou para a segunda etapa!')
    n3 = float(input('Nota: '))
    if n3 >= 8:
        print('Parabéns, você foi aprovado no concurso!')
    else:
        print('Que pena! Você não foi aprovado :(')
else:
    print('Que pena! Você não foi aprovado.')