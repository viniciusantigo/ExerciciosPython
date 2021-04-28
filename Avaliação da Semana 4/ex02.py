'''Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m2 deve-se usar 18w de potência.

Escreva um programa que receba a largura e o comprimento de um cômodo (em metros), calcule e mostre a sua área 
(em m2) e a potência de iluminação que deve ser utilizada.'''

larg = int(input('Informe a largura: '))
comp = int(input('Informe o comprimento: '))
area = larg * comp
potencia = area * 18
print(f'A área é igual a {area}m²')
print(f'E a potência utilizada será de {potencia}w')
