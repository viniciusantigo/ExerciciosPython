'''Faça um programa que calcule e mostre o fatorial de um número N, fornecido
pelo usuário. A definição de fatorial é mostrada a seguir:'''

multiplicador = 1

n = int(input('Informe um número: '))
print(f'{n}! = ', end='')

for i in range(1, n + 1): 
    valores = i
    multiplicador = multiplicador * i
    print(valores, end='')

    if i < n:
        print(' x ', end='')
    else: 
        print(' = ', end='')
        
print(multiplicador)