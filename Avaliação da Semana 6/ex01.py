'''Numa fábrica trabalham homens e mulheres divididos em duas classes:

Classe A: os que fazem até 30 peças por mês;
Classe B: os que fazem mais de 30 peças por mês.
A classe A recebe um salário-mínimo. A classe B recebe um salário-mínimo e mais R$ 10,00 por cada peça acima das 
30 iniciais.

Escreva um programa que leia a matrícula do operário e o número de peças fabricadas por ele no mês.
Como resposta mostre a matrícula do operário, sua classe e o salário que ele deve receber.'''

matricula = int(input('Informe sua matrícula: '))
pecas = int(input('Informe o número de peças fabricadas: '))
salario = 1100
print(f'Matrícula: {matricula}')
if pecas <=30: 
	print('Classe: A')
	print(f'Salário que deve receber: R${salario:.2f}')
else: 
	pecas_extras = pecas - 30
	salario_adicional = pecas_extras * 10
	print('Classe: B')
	print(f'Salário que deve receber: R${salario + salario_adicional:.2f}')
