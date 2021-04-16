'''2. Faça um programa que leia vários números, calcule e exiba a média desses
números.
Obs: a leitura do número 999 indica o fim dos dados de entrada e não deve ser
computado na média)'''

soma = 0
cont = 0

while True: 
    num = int(input('Informe um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
    media = soma / cont
print('A soma dos números é:', soma) 
print(f'E a média é: {media:.1f}')