'''1. Faça um programa que leia 30 números inteiros, calcule e mostre a soma deles
Obs: não use o comando for, use while.'''

cont = 0
soma = 0

while cont != 5: 
    num = int(input('Informe um número: '))
    cont += 1
    soma += num
print('A soma de todos os números informados é:', soma)