'''1. Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
semana (sábado e domingo). Considere que o dia 1 é o domingo.'''

dia = int(input('Informe um número de 1 a 7: '))

if dia >= 2 and dia < 7:
    print('Dia útil')

if dia == 1:
    print('Fim de semana. Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terça-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5: 
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta-Feira')
elif dia == 7:
    print('Fim de semana. Sábado')
else:
    print('Número inválido.')