'''Escreva um programa que leia o peso (kg) e a altura (m) de uma
pessoa, determine e mostre o seu grau de obesidade, de acordo com a
tabela seguinte. O grau de  obesidade é determinado pelo índice de
massa corpórea, cujo cálculo é realizado dividindo-se o peso da pessoa
pelo quadrado da sua altura.'''

altura = float(input('Entre com sua altura: '))
peso = float(input('Entre com seu peso: '))
imc = peso / altura ** 2
print(f'Seu índice de massa corporal é {imc:.2f}') 
if imc < 26:
 print('Seu IMC está normal.')
elif imc >= 26 and imc < 30:
 print('Você está obeso.')
elif imc >= 30:
 print('Você está com obesidade mórbida.')
