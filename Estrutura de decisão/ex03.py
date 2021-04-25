'''3. Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles.'''

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

if n1 > n2 and n1 > n3: 
	print(f'O maior é: {n1}')
elif n2 > n1 and n2 > n3:
	print(f'O maior é: {n2}')
elif n3 > n1 and n3: 
	print(f'O maior é: {n3}')
else: 
	print('Os números são iguais.')
	