'''6. Faça um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do
dólar e também a quantidade de dólares disponíveis com o usuário.'''

dolar = float(input('Valor da cotação do dólar: R$'))
usuario = float(input('Quantos dólares o usuário possui: US$'))
conversao = usuario * dolar
print(f'O usuário possui US${usuario:.2f} e a cotação do dólar está R${dolar:.2f}. A conversão é R${conversao:.2f}')
