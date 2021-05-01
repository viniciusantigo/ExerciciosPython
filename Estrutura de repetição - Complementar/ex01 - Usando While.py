'''1. Faça um programa que leia um número N, calcule e mostre os N primeiros
termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...). 
O valor lido para N sempre será maior ou igual a 2.'''

n = int(input('Informe um número: '))

t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2 
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Final')