#primeiro comando em Python

print('Hello World')

#variáveis 
nome = "Guanabara"
idade = 25
peso = 75.8
print(nome, idade, peso)
#função input
nome = input ('Qual é o seu nome? ')
idade = input ('Qual é a sua idade? ')
peso = input ('Qual é o seu peso? ')
print(nome, idade, peso)

#Desafio 1 aula 4
#Crie um programa que leia o nome de uma pessoa e mostre 
# uma mensagem de boas-vindas, de acordo com o valor digitado.

nome = input ('qual é o seu nome? ')
print('Seja bem vindo(a)', nome)

#Desafio 2 aula 4
#Crie um programa que leia o dia, o mês e o ano de nascimento de uma
#pessoa e mostre uma mensagem com a data formatada.

dia = input ('Digite o dia do seu nascimento: ')
mes = input ('Digite o mês do seu nascimento: ')
ano = input ('Digite o ano do seu nascimento: ')

print('Você nasceu no', dia, 'de', mes, 'de', ano,'.correto?')

#Desafio 3 aula 4
#Crie um programa que leia dois números e mostre a soma entre eles.
num1 = int(input('Digite o Primeiro Numero: '))
num2 = int(input('Digite o Segundo Numero: '))
print('A Soma dos Numeros é:', num1 + num2)