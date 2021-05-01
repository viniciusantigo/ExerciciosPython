'''1. Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...).
O valor lido para N sempre será maior ou igual a 2.'''

n = int(input('Informe um número: '))
t1 = 0
t2 = 1

print('Sequência de Fibonacci:',t1, t2, end=' ')

for i in range(3, n + 1):
    t3 = t1 + t2 
    print(t3, end=' ')
    t1 = t2
    t2 = t3
