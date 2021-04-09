'''Faça um programa que leia 20 números inteiros, determine e mostre o maior
deles.'''

maior = 0

for i in range(1, 6):
    n = int(input(f'Digite o {i}° número: '))
    if i == 0: 
        maior = n
    else: 
        if n > maior:
            maior = n
print(f'O maior é: {maior}')
