'''Escreva um programa que leia um vetor A de N números inteiros (N será lido) e
um outro inteiro K, construa e exiba um outro vetor B cujos elementos são os
respectivos elementos de A multiplicados por K.
Ex: A = [1,2,3], K = 5, B = [5,10,15].'''

n = int(input('Número de dígitos na lista: '))

a = [None] * n 
b = [None] * n

print('Digite os elementos do Vetor A: ')
for i in range(n):
    a[i] = int(input())

k = int(input('Digite o valor de K: '))

for i in range(n):
    b[i] = a[i] * k

print()
print('A =', a)
print('K =', k)
print('B =', b)
