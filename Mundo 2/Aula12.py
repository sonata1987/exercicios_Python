#Condições Aninhadas

#Exemplo:
# nome = str(input('Qual é o seu nome? '))
# if nome == "Gustavo":
#     print('Que nome lindo você tem ')
# elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
#     print('Seu nome é bem popular no Brasil.')
# elif nome in 'Ana Claudia Julia Juliana':
#     print('Belo nome feminino!')
# else:
#     print('Seu nome é tão normal!')

# print(f' Tenha um bom dia, {nome}!')

#Desafio 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de 
# uma casa. O programa vai perguntar o valor da casa, 
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 
# 30% do salário ou então o empréstimo será negado.

# valorcasa = float(input('Digite o valor da casa:  '))
# salario = float(input('Digite o seu salario atual: '))
# tempo = int(input('Em quantos anos vai pagar?: '))
# tempoemmeses = tempo*12
# prestacao = valorcasa / tempoemmeses

# print(f'30% do seu salario é R$ {(salario/30)*100:.2f}')

# if prestacao <= (salario / 30) * 100:
#     print(f'O valor da prestação será de R$ {prestacao:.2f} ao mes ')
#     print(f'Seu financiamento foi aprovado e será de {tempoemmeses:.0f} meses ')
# else:
#     print(f' Seu emprestimo foi negado! pois o valor da prestação de R$ {prestacao:.2f} excede 30% do seu salario')



#Desafio 37
#Escreva um programa que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

# num = int(input('Digite um numero inteiro qualquer: '))
# escolha = int(input('Digite um numero para selecionar a conversão \n 1 -para binário \n 2 -para octal \n 3 -para hexadecimal :'))

# if escolha == 1:
#     numbin = bin(num)
#     print(f' O numero {num} em binário é {numbin}')
# elif escolha == 2:
#     numoct = oct(num)
#     print(f' O numero {num} em octal é {numoct}')
# elif escolha ==3:
#     numhexa = hex(num)
#     print(f' O numero {num} em hexadecimal é {numhexa}')
# else:
#     print('Digite uma opção válida')


#desafio 38
#Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
# num1 = int(input('Digite o primeiro numero: '))
# num2 = int(input('Digite o segundo numero: '))

# if num1 > num2:
#     print(f' o primeiro numero {num1} é maior que o segundo numero {num2} ')
# elif num2 > num1:
#     print(f' o segundo numero {num2} é maior que o primeiro {num1} ')
# else:
#     print(f' os numeros {num1} e {num2} são iguais' )

#Desafio 39
#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# ano_nascimento = int(input('Digite o ano do seu nascimento: '))
# anoatual = 2025
# idade = anoatual - ano_nascimento
# idadealistamento = 18

# print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {anoatual} ')

# if idade < idadealistamento:
#     print(f'Faltam {idadealistamento - idade} ano(s) para você se alistar.')
# elif idade == idadealistamento:
#     print('Você precisa se alistar, chegou a sua hora!')
# else:
#     print(f'Já se passaram {idade - idadealistamento} ano(s) desde o seu alistamento.')


#desafio 40
#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# nota1 = float(input('Digite a primeira nota: '))
# nota2= float(input('Digite a segunda nota: '))
# media = (nota1 + nota2)/2

# if media < 5:
#     print('Reprovado')
# elif media >= 5 and media <= 6.9:
#     print('Recuperação')
# else:
#     print('Aprovado')

#Desafio 41
#A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima de 20 anos: MASTER

# anonascimento=int(input('Digite o ano do seu nascimento: '))
# anoatual = 2025
# idade = anoatual - anonascimento

# print(f'Sua idade é de {idade} anos portanto você está na categoria: ')

# if idade <= 9:
#     print('Mirim')
# elif idade >9 and idade <= 14:
#     print('Infantil')
# elif idade >14 and idade <= 19:
#     print ('Junior')
# elif idade > 19 and idade <= 20:
#     print ('Senior')
# else:
#     print ('Master')
    

#Desafio 42
#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

# lado1 = int(input('Digite um lado do triangulo: '))
# lado2 = int(input('digite o outro lado do triangulo: '))
# lado3 = int(input('Digite o terceiro lado do triangulo: '))

# if lado1 == lado2 and lado1 == lado3:
#     print('Este triangulo é um equilatero')
# elif lado1 == lado2 and lado2 != lado3:
#     print ('Este triangulo é Isoceles')
# else: 
#     print('este trinagulo é um escaleno')

#Desafio 43
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

# peso = float(input('Digite seu peso em kg: '))
# altura = float(input('Digite sua altura em mts: '))
# imc = peso / (altura*altura)
# print(f'Seu IMC é de {imc:.0f} ')

# if imc < 18.5:
#     print('abaixo do peso')
# elif imc >= 18.5 and imc < 25:
#     print('Peso ideal')
# elif imc >= 25 and imc < 30:
#     print ('Sobrepeso')
# elif imc >= 30 and imc < 40:
#     print('Obesidade')
# else:
#     print('Obesidade morbida')

#Desafio 44
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
# valor = float(input('Digite o valor do produto: '))
# formapgto = int(input('digite a forma de pagamento: \n 1 - para a dinheiro/cheque à vista \n 2 - para a vista cartão de crédito \n 3 - 2x no cartão de crédito \n 4 - 3x ou mais no cartão de crédito '))

# if formapgto == 1:
#     valordesconto = valor/10
#     print(f'O valor do desconto é de R$ {valordesconto:.2f}')
#     valor = valor - valordesconto
#     print(f'O valor do Seu produto com desconto de 10%  ficará em R$ {valor:.2f}')
# elif formapgto ==2:
#     valordesconto = (valor * 5) / 100
#     print(f'O valor do desconto é de R$ {valordesconto:.2f}')
#     valor = valor - valordesconto
#     print(f'O valor do Seu produto com desconto de 5%  ficará em R$ {valor:.2f}')
# elif formapgto ==3:
#     print(f'O valor do seu produto é de R$ {valor:.2f} e você não tera desconto ')
# elif formapgto == 4:
#     qtdevezes = int(input('Você pretende pagar em quantas vezes?: '))
#     if qtdevezes >= 3:
#         print('Você escolheu pagar em 3x ou mais no cartão de crédito')
#         valorjuros = valor * 0.20
#         valor = valor + valorjuros
#         print(f' Você terá um acréscimo de 20% de juros e o novo valor é de R$ {valor:.2f} ')
#     else:
#         print(f'O valor do seu produto é de R$ {valor:.2f} e você não terá desconto ')
# else:
#     print('Forma de pagamento inválida, tente novamente!')

#Desafio 45
#Crie um programa que faça o computador jogar Jokenpô com você. 
# import random

# escolhajog = int(input('Escolha: \n 1- Pedra \n 2- Papel \n 3 - Tesoura \n: '))
# escolhapc = random.randint(1,3)

# if escolhajog ==1 and escolhapc == 1 or escolhajog ==2 and escolhapc == 2 or escolhajog ==3 and escolhapc == 3:
#     print(f'Computador escolheu {escolhapc} e você escolheu {escolhajog}')
#     print('Empate')
# elif escolhajog ==1 and escolhapc == 3 or escolhajog ==2 and escolhapc == 1 or escolhajog ==3 and escolhapc == 2:
#     print(f'Computador escolheu {escolhapc} e você escolheu {escolhajog}')
#     print('Jogador Venceu')
# else:
#     print(f'Computador escolheu {escolhapc} e você escolheu {escolhajog}')
#     print('Computador Venceu')



