#manipulando texto
# #Aula 9
# frase = 'Curso em video python'
# print(frase)
# print(frase[9]) #imprime a letra na posição 9
# print(frase[9:13]) #imprime da posição 9 até a 13
# print(frase[9:21:2]) #imprime da posição 9 até a 20 pulando de 2 em 2
# print(frase[:5]) #imprime do inicio até a posição 4
# print(frase[15:]) #imprime da posição 15 até o final
# print(frase[9::3]) #imprime da posição 9 até o final pulando de 3 em 3
# print(len(frase)) #imprime o tamanho da frase
# print(frase.count('o')) #imprime quantas vezes a letra o aparece na frase
# print(frase.count('o',0,13)) #imprime quantas vezes a letra o aparece na frase da posição 0 até a 12
# print(frase.find('deo')) #imprime a posição onde começa a palavra deo
# print(frase.find('Android')) #imprime -1 pois não existe a palavra
# print('Curso' in frase) #imprime True   #pois a palavra Curso existe na frase
# #Transformação de strings
# print(frase.replace('python','android')) #substitui a palavra python por android
# #upper  - deixa todas as letras maiusculas
# print(frase.upper())
# #lower - deixa todas as letras minusculas
# print(frase.lower())
# #capitalize - deixa apenas a primeira letra maiuscula
# print(frase.capitalize())
# #title - deixa todas as primeiras letras de cada palavra maiusculas
# print(frase.title())
# #strip - remove todos os espaços inúteis no começo e no final da frase
# frase2 = '   Aprenda Python  '
# print(frase2)
# print(frase2.strip())
# #lstrip - remove os espaços inúteis apenas do lado esquerdo
# print(frase2.lstrip())
# #rstrip - remove os espaços inúteis apenas do lado direito
# print(frase2.rstrip())
# #Divisão de strings
# print(frase.split()) #divide a frase em várias partes e cria uma lista
# #Junção de strings
# print('-'.join(frase)) #junta todas as letras da frase separando por -
# print('-'.join(frase.split())) #junta todas as palavras da frase separando por --

#Desafio 22
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1 - O nome com todas as letras maiúsculas
#2 - O nome com todas as letras minúsculas
#3 - Quantas letras ao todo (sem considerar espaços)
#4 - Quantas letras tem o primeiro nome

# nomecompleto = str(input('Digite seu nome completo: '))
# print(nomecompleto.upper())
# print(nomecompleto.lower())
# print(len(nomecompleto.replace(" ", "")))
# print(len(nomecompleto.split()[0]))

#desafio 23
# Crie um programa que leia um número de 0 a 9999 e mostre na tela 
# cada um dos dígitos separados.
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1 
# num= str(input('Digite um numero de 0 a 9999: '))
# print(f'Unidade:  {num[3]}')
# print(f'Dezena:  {num[2]}')
# print(f'Centena:  {num[1]}')
# print(f'Milhar:  {num[0]}')

#desafio 24
# # Crie um programa que leia o nome de uma cidade diga se ela começa ou não com  o nome "SANTO".
# cidade= str(input('Digite o nome da cidade: ')).strip()
# print(cidade[:5].upper() == 'SANTO')


#desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
# nome= str(input('Digite o nome: '))
# print('SILVA' in nome.upper())


#desafio 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez 
# frase= str(input('Digite uma frase qualquer: '))
# print(f'A frase "{frase}" contém a letra "A" {frase.upper().count("A")} vezes')
# print(f'A Letra "A" aparece pela primeira vez na posição {frase.upper().find("A")}')
# print (f'A Letra "A" aparece pela ultima vez na posição {frase.upper().rfind("A")}')

#desafio 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e
# o último nome separadamente.
nome= str(input('Digite seu nome completo: '))
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}')
print(f'Seu ultimo nome é {separa[-1]}')
