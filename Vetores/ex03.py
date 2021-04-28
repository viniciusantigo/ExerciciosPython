'''3. Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece.'''

n = int(input('Informe o tamanho do vetor V: '))
v = [None] * n

print('Informe os elementos do vetor V: ')
for i in range(n):
    v[i] = int(input())

k = int(input('Digite o valor de K: '))

existe = False

for e in v: 
    if e == k: 
        existe = True
        break

if existe:
    print(f'O valor de {k} está no vetor nas seguintes posições:')
    for i in range(n):
        if v[i] == k:
            print(i)
else:
    print(f'O valor de {k} não está no vetor.')