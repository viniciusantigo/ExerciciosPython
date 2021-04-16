'''5. Faça um programa que leia um número inteiro e determine se ele é par ou
ímpar. Ao final, o programa deve perguntar se o usuário deseja continuar
(digitar outro número) ou sair. Se o usuário quiser continuar, o programa deve
repetir tudo de novo, caso contrário o programa deve ser encerrado.'''

while True: 
    usuario = int(input('Digite um número: '))
    
    if usuario % 2 == 0:
        print('O número informado é PAR.')
    else:
        print('O número informado é ÍMPAR.')

    pergunta = input('Deseja continuar? (s / n) ').lower()
    if pergunta == 'n':
        break