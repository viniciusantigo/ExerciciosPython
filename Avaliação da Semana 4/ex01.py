'''Todo e-mail é formado por duas partes: o login do usuário e o domínio do provedor.

Veja o exemplo abaixo:

E-mail: antonio.silva@ifpb.edu.br
Login: antonio.silva
Domínio: ifpb.edu.br

Escreva um programa que leia o login de um usuário e o domínio do seu provedor e mostre o seu e-mail completo.'''

login = input('Informe seu login: ')
dominio = input('Informe o domínio: ')
print(login, dominio, sep='@')