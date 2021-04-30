'''5. Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os
seus coeficientes. Fórmulas:

Obs: se Δ for negativo, não existem as raízes da equação.
Dica: use a função sqrt do módulo math.'''

from math import sqrt

print('Resolução de uma equação de segundo grau!')
a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

delta = b ** 2 - 4 * a * c
x1 = (- b + sqrt(delta)) / (2 * a) 
x2 = (- b + sqrt(delta)) / (2 * a)
print('Valor de delta:',delta)
if delta < 0: 
    print('As raízes da equação não existem pois o delta é negativo')
else:
    print(f'As raízes da equação são {x1:.1f} e {x2:.1f}')
