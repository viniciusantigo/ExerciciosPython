'''4. Escreva um programa que leia a hora de início de um jogo e a hora do final do jogo (considerando
apenas horas inteiras), calcula a duração do jogo em horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
O programa deve mostrar o resultado obtido.'''

hora_inicio = int(input('Hora de início: '))
hora_final = int(input('Hora do término: '))

if hora_inicio < hora_final:
    tempo = hora_final - hora_inicio
else:
    tempo = 24 - hora_inicio + hora_final

print('Duração:',tempo,'horas')