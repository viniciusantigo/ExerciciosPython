'''2. Escreva um programa que solicite a digitação de um caractere qualquer do teclado e imprima
sua classificação: vogal, consoante, número e caractere especial.'''

caractere = input('Informe um caractere qualquer: ').lower()
print('Classificação: ', end='')
if caractere >= 'a' and caractere <= 'z':
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
        tipo = 'vogal'
    else:
        tipo = 'consoante'

elif caractere >= '1' and caractere <= '9':
    tipo = 'número'
else:
    tipo = 'caractere especial'

print(tipo)