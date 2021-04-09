'''Faça um programa que, para um grupo de N pessoas (obs: N será lido):
• Leia o sexo (M ou F) de cada pessoa;
• Calcule e escreva o percentual de homens;
• Calcule e escreva o percentual de mulheres.'''

cont_mulher = 0
cont_homem = 0

n = int(input('Informe a quantidade de pessoas que participarão do teste: '))

for i in range(n):
    sexo = input('Informe o sexo: (M ou F) ').upper()
    
    if sexo == 'F':
        cont_mulher += 1
    else:
        cont_homem += 1
    
    porcent_mulher = (cont_mulher / n) * 100
    porcent_homem = 100 - porcent_mulher

print(f'{n} pessoas foram cadastradas.')
print(f'{porcent_mulher:.0f}% são mulheres e {porcent_homem:.0f}% são homens.')