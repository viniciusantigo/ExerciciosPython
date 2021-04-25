'''2. Escreva um programa que leia dois números e exiba-os em ordem crescente.'''

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

if n1 > n2:
	print(f'{n2} -> {n1}')
elif n1 == n2: 
	print('Os números informados são iguais.')
else: 
	print(f'{n1} -> {n2}')
