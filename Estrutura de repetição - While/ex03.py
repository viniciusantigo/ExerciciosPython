'''3. Faça um programa que leia vários números, determine e mostre o maior e o
menor deles.
Obs: a leitura do número 0 (zero) encerra o programa.'''

flag = 0
print('A entrada do número 0 (zero) encerrará o programa.')

num = int(input())

maior = num
menor = num

while num != flag:

    if num > maior:
        maior = num
    if num < menor: 
        menor = num
    
    num = int(input())

print('O maior é:', maior)
print('O menor é:', menor)
