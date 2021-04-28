'''Faça um programa que apresente o menu de opções abaixo:

OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM

O programa deve ler a opção do usuário e exibir, para cada opção, a respectiva mensagem:

1 - Olá. Como vai?
2 - Vamos estudar mais.
3 - Meus Parabéns!
0 - Fim de serviço.

Enquanto a opção for diferente de 0 (zero) deve-se continuar apresentando o menu de opções.'''

print('''Opções: 
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')

while True:
	opcao = int(input('Informe a opção desejada: '))
	if opcao == 0:
		print('Fim de serviço.')
		break
	elif opcao == 1:
		print('Olá, como vai?')
	elif opcao == 2:
		print('Vamos estudar mais.')
	elif opcao == 3:
		print('Meus parabéns!')
	else: 
		print('Informe um número válido.')
	print('--' * 15)