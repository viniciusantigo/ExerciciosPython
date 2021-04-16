'''Faça um programa que leia um número inteiro N, calcule e mostre o maior
quadrado perfeito menor ou igual a N. Por exemplo, se N for igual a 38, o
resultado é 36.'''
import math

maior = 0

n = int(input('Informe um número: '))

for i in range(1, n + 1):
    raiz = math.sqrt(i)
    if raiz == int(raiz) and i > maior:
        maior = i 

print('Maior quadrado perfeito:', maior)