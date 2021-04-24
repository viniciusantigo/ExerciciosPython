'''4. Um motorista anota a marcação do hodômetro do seu veículo antes e após uma viagem,
bem como o número de litros de combustível gastos.
Escreva um programa que leia os 3 dados acima, o preço do litro de combustível, a
capacidade do tanque e mostre:
a) Quilometragem rodada.
b) Quantos quilômetros por litro faz o veículo.
c) Autonomia do veículo.
d) Custo da viagem.'''

km_inicial = int(input('Odômetro inicial (Km): '))
km_final = int(input('Odômetro final (Km): '))
comb_gasto = int(input('Quantidade gasta de combustível (litros): '))
preco_litro = float(input('Preço do litro do combustível (R$): '))
cap_tanque = int(input('Capacidade do tanque (litros): '))

km_rodada = km_final - km_inicial
consumo = km_rodada / comb_gasto
autonomia = consumo * cap_tanque
custo_viagem = comb_gasto * preco_litro

print(f'\nQuilometragem rodada: {km_rodada} km')
print(f'Consumo: {consumo:.1f} km/L')
print(f'Autonomia: {autonomia:.0f} km')
print(f'Custo da viagem: R$ {custo_viagem:.2f}')