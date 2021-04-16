'''4. Faça um programa que leia os seguintes dados de um conjunto de alunos:
matrícula, nome e as duas notas que ele obteve em suas avaliações. A
condição de parada será a digitação de uma matrícula igual 0 (zero). O
programa deverá mostrar, para cada aluno, as seguintes informações:
matrícula, nome, média e situação (aprovado, se a média for igual ou superior
a 7 e, reprovado, se a média for inferior a 7).'''


while True:

    print('Entrada da matrícula com valor 0 (zero) encerrará o programa.')

    matricula = int(input('Informe a matrícula do(a) aluno(a): '))
    if matricula == 0:
        break

    nome = input('Informe o nome do(a) aluno(a): ')
    a1 = float(input('Primeira nota: '))
    a2 = float(input('Segunda nota: '))

    media = (a1 + a2) / 2

    print('--' * 20)
    print('Matrícula:', matricula)
    print('Nome do(a) aluno(a):', nome)
    print('Média:', media)
    if media >= 7:
        print('Aprovado!')
    else:
        print('Reprovado.')
    print('--' * 20)
