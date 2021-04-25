'''5. A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma
comissão de 5% sobre o total de vendas daquele vendedor, mas essa
comissão nunca deve ser inferior ao salário-mínimo.
Escreva um programa que leia o valor total das vendas de um
vendedor e escreva seu salário.'''

totvenda = int(input('Informe o total de vendas: '))
salario = 1045
comissao = totvenda * (salario * (5 / 100))
if comissao < salario:
 print(f'Seu salário é R${salario:.2f}')
else:
 print(f'Seu salário é R${comissao + salario:.2f}') 
 