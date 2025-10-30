#laços de repetição
#for
# for i in range(11):
#     print(i)
# print('Acabou')

#desafio 46
#faça um programa que mostre na tela uma contagem regressiva para o estouro 
# de fogos de artifício, indo de 10 até 0, 
# com uma pausa de 1 segundo entre eles.
# import time
# for i in range (11,0,-1):
#     time.sleep(1)
#     print(i -1)
# print('FELIZ ANO NOVO!!!')

#desafio 47
# crie um programa que mostre na tela todos os números 
# pares que estão no intervalo entre
# 1 e 50.
# for i in range(1,50):
#     if i % 2 == 0:
#         print(i)

#desafio 48
# faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

# soma=0

# for i in range (1,501):
#     if i% 2 != 0 and i % 3==0:
#         print(i)
#         soma += i
# print(f' a soma dos números é de {soma}')

#desafio 49
# refaça o desafio 9, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for.

# numero = int(input('Digite o numero a ser calculado: '))
# resultado = 0
# for i in range(0,11):
#     resultado = numero * i
#     print(f' {numero} X {i} = {resultado}')

#desafio 50
# desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado for
# ímpar, desconsidere-o.
# numero = 0
# for i in range(0,6):
#     i = int(input('Digite os numeros a serem calculados: '))
#     if i % 2 == 0:
#         numero +=i 
        
# print(f'A soma dos números pares digitados é {numero}')

#desafio 51
# desenvolva um programa que leia o primeiro termo e a razão de
# uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# primeiro = int(input('Primeiro termo:'))
# razão = int(input('Razão:'))
# decimo = primeiro + (10 - 1) * razão
# for i in range(primeiro, decimo + razão, razão):
#     print(i, end=' -> ')
# print('ACABOU') 


#desafio 52
# faça um programa que leia um número inteiro e diga se ele é ou
# não um número primo.
# num = int(input('Digite um número: '))
# if num > 1:
#     for i in range(2,num):
#         if (num % i) ==0:
#             print(f' {num} não é um numero primo')
#             break
#     else:
#         print(f' {num} é um numero primo')
# else:
#     print(f' {num} não é um numero primo')

#desafio 53
# crie um programa que leia uma frase qualquer e diga se ela é
# um palíndromo, desconsiderando os espaços.

#minha solução
frase = str(input('Digite uma frase: '))

for letra in frase: 
    frasemin = frase.lower()
    frase2 = frasemin.replace(" ","")
    frasein = frase2[::-1]
    print(f'A frase "{frase}" sem espaços fica: {frase2}')
    print (f'A frase "{frase}" invertida fica {frasein}')
    if frase2 == frasein:
        print('É um palindromo!')
    else:
        print('Não é um palindromo')
    break

#solução do professor
# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]
# print(f'O inverso de {junto} é {inverso}')
# 


#desafio 54
# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

#desafio 55
# faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.

#desafio 56
# desenvolva um programa que leia o nome, idade e sexo de 4
# pessoas. No final do programa, mostre:
# a média de idade do grupo;
# qual é o nome do homem mais velho;
# quantas mulheres têm menos de 20 anos.    