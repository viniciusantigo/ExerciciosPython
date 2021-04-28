'''Em uma pesquisa foram coletados os seguintes dados de um conjunto de várias pessoas:

Idade;
Sexo (M-masculino ou F-feminino);
Estado Civil (S-solteiro, C-casado, V-viúvo ou D-divorciado).
Neste contexto, faça um programa que leia os dados coletados durante a pesquisa, determine e mostre:

a) O percentual de mulheres;
b) O percentual de homens;
c) A média de idade das pessoas;
d) A quantidade de mulheres solteiras com idade inferior a 20 anos;
e) A quantidade de homens casados com idade superior a 30 anos.

Obs: a leitura da idade 0 (zero) indicará o fim dos dados de entrada (flag) e não deve ser contabilizada.'''

cont_pessoas = 0
cont_mulher_solteira = 0
cont_mulher = 0
cont_homem = 0
cont_homem_casado = 0
cont_idade = 0

print('''Bem-vindo à pesquisa!
Digitar 0 (zero) no campo de idade encerrará a coleta de dados.''')

while True:

	idade = int(input('Idade: '))
	sexo = input('Sexo: (M ou F) ').upper()
	estcivil = input('Estado civil: ').upper()
	print('--' * 10)
	if idade > 0: 
		cont_pessoas += 1
		cont_idade += idade
	else:
		break

	if sexo == 'F': 
		cont_mulher += 1
	else: # Pressupondo que o usuário não informe outra letra. 
		cont_homem += 1

	# Calculando porcentagem de homens e mulheres
	porct_mulher = (cont_mulher / cont_pessoas) * 100
	porct_homem = 100 - porct_mulher

	# Calculando a média de idade
	media_idade = cont_idade / cont_pessoas

	# Calculando mulheres solteiras com idade inferior a 20
	if sexo == 'F' and estcivil == 'S' and idade < 20:
		cont_mulher_solteira += 1

	# Calculando homens casados com idade superior a 30
	if sexo == 'M' and estcivil == 'C' and idade > 30: 
		cont_homem_casado += 1

print(f'O percentual de mulheres é: {porct_mulher:.0f}%')
print(f'O percentual de homens é: {porct_homem:.0f}%')
print(f'A média de idade geral é: {media_idade:.0f}')
print(f'Mulheres solteiras de até 20 anos: {cont_mulher_solteira}')
print(f'Homens casados com mais de 30 anos: {cont_homem_casado}')