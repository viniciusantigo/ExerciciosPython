'''2. Escreva um programa para calcular e exibir a média ponderada de 2 notas dadas. Sabe-
se que nota1 possui peso 6 e nota2 possui peso 4.'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 * 6 + n2 * 4) / 10
print(f'Sua média é: {media :.1f}')