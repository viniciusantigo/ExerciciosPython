'''Escreva um programa que tenha a funcionalidade de uma calculadora
simples. O programa deve solicitar a digitação de dois operandos e um
operador (+ - x * / %) e deve imprimir ao resultado da operação
aritmética. Caso o usuário digite um operador inválido, o programa
deve imprimir "Operador desconhecido".'''

op1 = int(input('Informe o primeiro operando: '))
op2 = int(input('Informe o segundo operando: '))
operador = input('Informe o operador: (x, /, -, +, %) ')

if operador == 'x':
 print(op1 * op2)
elif operador == '/':
 print(op1 / op2)
elif operador == '-':
 print(op1 - op2)
elif operador == '+':
 print(op1 + op2)
elif operador == '%':
 print(op1 % op2)
else:
 print('Operador inválido.')