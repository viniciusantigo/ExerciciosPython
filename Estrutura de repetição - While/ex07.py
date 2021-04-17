'''7. Faça um programa que leia a idade de várias pessoas visitantes de um show (a
leitura da idade 0 indicará o fim dos dados de entrada), calcule e exiba:
• A média de idade do público;
• A porcentagem de pessoas com idade entre 18 e 21 anos;
• Idade do visitante mais jovem.'''

cont_idade = 0
porct_idade = 0 
cont_pessoas = 0

idade = int(input('Informe sua idade: '))
menor = idade

while True:
    
    cont_idade += idade
    if idade == 0:
        break
    if idade >= 18 and idade <= 21:
        porct_idade += 1
    if idade < menor: 
        menor = idade
    idade = int(input('Informe sua idade: '))
    cont_pessoas += 1

    porct = (porct_idade / cont_pessoas) * 100


media = cont_idade / cont_pessoas
print('A menor idade é:', menor)
print(f'A média de idade das pessoas é: {media:.1f}')
print(f'A porcentagem de pessoas com idade entre 18 e 21 anos é: {porct:.0f}%')