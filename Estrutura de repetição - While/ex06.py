'''6. Chico tem 1,50 metros e cresce 2 centímetros por ano, enquanto Zé tem 1,10
metros e cresce 3 centímetros por ano. Faça um programa que calcule e
imprima quantos anos serão necessários para que Zé seja maior que Chico.'''

chico = 1.50
ze = 1.10
cont_anos = 0

while ze <= chico:
    cont_anos += 1
    ze += 0.03
    chico += 0.02

print(f'Zé levou {cont_anos} anos para ultrapassar Chico em altura, Chico tem {chico:.2f}m e Zé tem {ze:.2f}m')
