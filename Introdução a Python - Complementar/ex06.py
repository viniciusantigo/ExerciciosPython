'''As Ilhas Weblands formam um reino independente nos mares do Pacífico. Como é um reino recente, a sociedade é muito influenciada pela informática. A moeda oficial é o Bit; existem notas de B$ 50, B$ 10, B$ 5 e B$ 1.

Você foi contratado(a) para ajudar na programação dos caixas automáticos de um grande banco das Ilhas Weblands.

Os caixas eletrônicos das Ilhas Weblands operam com todos os tipos de notas disponíveis, mantendo um estoque para cada valor de cédula. Os clientes do banco utilizam os caixas eletrônicos para efetuar retiradas de um certo número inteiro de Bits.

Sua tarefa é escrever um programa que, dado o valor de Bits desejado pelo cliente, determine o número de cada uma das notas necessário para totalizar esse valor, de modo a minimizar a quantidade de cédulas entregues.

Exemplo:

Para B$ 72 seriam as seguintes notas:

1 nota(s) de B$ 50
2 nota(s) de B$ 10
0 nota(s) de B$ 5
2 nota(s) de B$ 1'''

x = int(input("Digite o valor: B$ "))

n50 = x // 50
r = x % 50
n10 = r // 10
r = r % 10
n5 = r // 5
r = r % 5
n1 = r

print(n50,"nota(s) de B$ 50")
print(n10,"nota(s) de B$ 10")
print(n5,"nota(s) de B$ 5")
print(n1,"nota(s) de B$ 1")