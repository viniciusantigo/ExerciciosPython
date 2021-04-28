'''Escreva um programa para calcular a conta final de um hóspede de um hotel, considerando que:

Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede;
O valor da diária é determinado pela seguinte tabela:

O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
O valor da taxa de serviço equivale a 10% do subtotal;
O total geral resulta da soma do subtotal com a taxa de serviço.
O programa deverá mostrar a conta final do hóspede, contendo: o nome do hóspede, o tipo do apartamento, o número de diárias utilizadas, o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total geral.'''

nome = input('Informe o nome do cliente: ')
tipo_ap = input('Informe o tipo do apartamento: ').upper()
diarias = int(input('Informe o número de diárias: '))
valor_consumo = float(input('Valor do consumo do cliente: R$'))

if tipo_ap == 'A': 
	valor = 150
	total_diarias = valor * diarias
elif tipo_ap == 'B':
	valor = 100
	total_diarias = valor * diarias
elif tipo_ap == 'C':
	valor = 75 
	total_diarias = valor * diarias
elif tipo_ap == 'D':
	valor = 50
	total_diarias = valor * diarias

sub_total = total_diarias + valor_consumo
taxa_serv = sub_total * (10 / 100)
total_geral = sub_total + taxa_serv

print(f'Nome do hóspede: {nome}')
print(f'Tipo de apartamento escolhido: {tipo_ap}')
print(f'Número de diárias utilizadas: {diarias}')
print(f'Valor unitário da díaria: R${valor:.2f}')
print(f'Valor total das diárias: R${total_diarias:.2f}')
print(f'Valor do consumo interno: R${valor_consumo:.2f}')
print(f'Subtotal: R${sub_total:.2f}')
print(f'Taxa de serviço: R${taxa_serv:.2f}')
print(f'Total: R${total_geral:.2f}')
