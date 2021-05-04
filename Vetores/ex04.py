'''4. Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
• Os números que estão nos índices pares;
• Os números que estão nos índices ímpares.'''

n = 10

vetor = [None] * n
print('Informe os números do vetor: ')
for i in range(n):
    vetor[i] = int(input())

print('Números que estão nos índices pares: ')
for i in range(n):
    if i % 2 == 0:
        print(vetor[i])

print('Números que estão nos índices ímpares: ')
for i in range(n):
    if i % 2 == 1:
        print(vetor[i])
