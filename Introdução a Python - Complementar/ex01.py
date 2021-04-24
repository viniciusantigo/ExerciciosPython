'''1. A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
valor da venda.
Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
vendas de um vendedor, e calcule e exiba o seu salário.'''

nome = input('Nome: ')
ncar = int(input('Carros vendidos: '))
valort = float(input('Valor total: R$'))
porct = valort * 5 / 100
salario = 1000 + ncar * 200 + porct
print(f'Salário: R${salario :.2f}')