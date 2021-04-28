'''2. Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.'''

v = [None] * 5

print('Digite os valores de V: ')
for i in range(5):
    v[i] = int(input())

k = int(input('Informe um número: '))

cont = 0

for e in v:
    if k == e:
        cont += 1
print('Quantidade de ocorrências de K dentro de V:', cont)