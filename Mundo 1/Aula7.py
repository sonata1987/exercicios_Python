# # #operadores aritméticos
# # # + adição
# # # - subtração
# # # * multiplicação
# # # / divisão
# # # ** potência
# # # // divisão inteira
# # # % resto da divisão


# # # ordem de precedência
# # # 1º ()
# # # 2º **
# # # 3º * / // %
# # # 4º + -

# # #Desafio 5
# # #Faça um programa que leia um numero inteiro e 
# # #mostre na tela seu sucessor e seu antecessor

# # num = int (input('digite um número inteiro:'))
# # print(f'Analisando o numero {num}, seu antecessor é {num -1} e seu sucessor é {num +1}')

# # #Desafio 6
# # #crie um algoritmo que leia um número e
# # #mostre o seu dobro, triplo e raiz quadrada

# # num = int (input(' Digite um número qualquer: '))
# # print (f' O dobro do número digitado é {num*2}, o triplo do número é {num*3} e a raiz quadrada é {num**(1/2)}')

# # #Desafio 7
# # #desenvolva um programa que leia as duas notas de um aluno,
# # #calcule e mostre a sua média
# # nota1 = float(input('Digite a primeira nota: '))
# # nota2 = float(input('Digite a segunda nota: '))

# # print(f'A média das notas é {(nota1 + nota2)/2}')

# # #Desafio 8
# # # Escreva um programa que leia um valor em metros e o 
# # # exiba convertido em centímetros e milímetros

# # valor_em_metros = float(input('Digite o valor em metros: '))
# # print(f' O valor em centimetros é {valor_em_metros * 100:.0f} e o valor em milimetros é {valor_em_metros * 1000:.0f}')

# # #desafio 9
# # # faça um programa que leia um número inteiro qualquer e
# # # mostre na tela a sua tabuada
# # num = int(input('Digite um numero inteiro qualquer para ver a sua tabuada: '))
# # print(f'A tabuada de {num} é: ') 
# # print(f' {num} X 0 = {num * 0}')
# # print(f' {num} X 1 = {num * 1}')
# # print(f' {num} X 2 = {num * 2}')
# # print(f' {num} X 3 = {num * 3}')
# # print(f' {num} X 4 = {num * 4}')
# # print(f' {num} X 5 = {num * 5}')
# # print(f' {num} X 6 = {num * 6}')
# # print(f' {num} X 7 = {num * 7}')
# # print(f' {num} X 8 = {num * 8}')
# # print(f' {num} X 9 = {num * 9}')
# # print(f' {num} X 10 = {num * 10}')


# # #Desafio 10
# # # Crie um programa que leia quanto dinheiro uma pessoa 
# # # tem na carteira e
# # # mostre quantos dólares ela pode comprar.
# # # Considere US$1,00 = R$3,27

# # valor_na_carteira = float (input('digite quanto você tem na carteira em reais :'))
# # print(f' Você pode comprar até {valor_na_carteira / 3.27:.2f} dolares')

# # #desafio 11
# # # faça um programa que leia a largura e a altura de uma parede em metros,
# # # calcule a sua área e a quantidade de tinta necessária para pintá-la,
# # # sabendo que cada litro de tinta pinta uma área de 2m².

# # largura = float(input('Digite a largura da parede :'))
# # altura = float(input('Digite a altura da parede :'))
# # area_parede = largura * altura
# # litros_tinta = area_parede / 2
# # print(f' Você precisará de {litros_tinta} litros de tinta para pintar a parede de {area_parede} m²')


# # #Desafio 12
# # # faça um algoritmo que leia o preço de um produto e
# # # mostre seu novo preço, com 5% de desconto.

# # preco_atual = float(input('Digite o preço atual do produto: '))
# # desconto = preco_atual * 0.05
# # preco_com_desconto = preco_atual - desconto

# # print(f'O preço original era R$ {preco_atual:.2f}, o desconto foi de R$ {desconto:.2f}, e o preço com desconto de 5% é R$ {preco_com_desconto:.2f}')

# # #desafio 13
# # # faça um algoritmo que leia o salário de um funcionário e
# # # mostre seu novo salário, com 15% de aumento.
# # salario_atual = float(input('Digite o seu salario atual: '))
# # aumento = salario_atual * 0.15
# # novo_salario = salario_atual + aumento

# # print(f'O seu salario novo será de R${novo_salario}')

# # #desafio 14
# # # Escreva um programa que converta uma temperatura digitada em °C
# # # e converta para °F.

# # celsius = float(input('digite a temperatura em Celsius:'))
# # fahrenheit = (celsius * 1.8) + 32
# # #formula para conversão (°C x 1,8) + 32
# # print (f' a temperatura de {celsius}ºC em Fº é de {fahrenheit}Fº') 

# #desafio 15
# # Escreva um programa que pergunte a quantidade de km
# # percorridos por um carro alugado e a quantidade de dias pelos quais
# # ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# # e R$0,15 por km rodado.

# qtdekm = float(input('digite a quantidade de KM percorrido: '))
# qtdedias = int(input('Digite a quantidade de dias de aluguel do veiculo: '))
# custokm = 0.15
# diariacarro = 60
# calculokm = qtdekm * custokm
# calculodiarias = qtdedias * diariacarro

# print(f'Você pagará um total de R${calculokm:.2f} pelos km rodados e um total de R${calculodiarias:.2f} pelos dias utilizados')