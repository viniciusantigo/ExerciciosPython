'''Faça um programa que leia um número N, inteiro, e some todos os números
de 1 até N, mostrando o resultado.'''

soma = 0

n = int(input('Informe um número: '))

for i in range(1, n + 1): 
    valores = i
    soma = soma + valores

    print(valores, end='')

    if i < n:
        print(' + ', end='')
    else:
        print(' = ', end='')

print(soma)