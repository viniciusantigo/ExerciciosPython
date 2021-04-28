'''Faça um programa para ler o nome e o salário bruto dos 100 funcionários de uma determinada empresa.
Para cada funcionário lido, o programa deverá emitir o respectivo contracheque, que deverá conter:
O nome do funcionário;
O valor do salário bruto;
O valor do desconto do INSS (12% do Salário Bruto)
O valor do salário líquido (Salário Bruto - Desconto INSS)
Ao final, o programa deverá mostrar:
A soma total dos salários brutos;
A soma total dos descontos do INSS;
A soma total dos salários líquidos.'''

total_bruto = 0
total_desconto = 0
total_liquido = 0
for i in range(3):
	nome = input('Nome: ')
	salario = float(input('Salário: R$'))
	desconto = (salario * (12 /100))
	salario_liquido = salario - desconto
	print(f'Nome: {nome}')
	print(f'Salário bruto: R${salario:.2f}')
	print(f'Desconto do INSS: R${desconto:.2f}')
	print(f'Salário líquido: R${salario_liquido:.2f}')
	print('--' * 20)
	if salario > 0: 
		total_bruto += salario
		total_desconto += desconto
		total_liquido += salario_liquido
print(f'Soma total dos salários brutos: R${total_bruto:.2f}')
print(f'Soma total dos descontos do INSS: R${total_desconto:.2f}')
print(f'Soma total dos salários líquidos: R${total_liquido:.2f}')
