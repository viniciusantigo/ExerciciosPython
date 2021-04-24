'''Escreva um programa que, dado um número inteiro representando uma quantidade de segundos, 
calcule quantas horas, minutos e segundos estão contidos nesta quantidade.

Ex: 7.388 segundos = 2 horas, 3 minutos e 8 segundos.'''

'''
7388 / 3600 = 2 h
resto = 188
188 / 60 = 3 m
resto = 8 s
'''

n = int(input('Quantidade de segundos: '))

h = n // 3600
m = (n % 3600) // 60
s = (n % 3600) % 60

print(f'Resultado: {h:02}:{m:02}:{s:02}')
