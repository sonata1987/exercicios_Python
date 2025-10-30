#tipos primitivos de dados e saída de dados

#desafio 1
#crie um programa que leia dois números e mostre a soma entre eles
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# s = n1 + n2
# print('A soma entre', n1, 'e', n2, 'vale', s)
#format string
# print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#desafio 2
#faça um programa que leia algo pelo teclado e 
# mostre na tela o seu tipo primitivo e 
# todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('o tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())
