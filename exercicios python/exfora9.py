#Desenvolva um programa que leia um número inteiro qualquer e 
# que apresete o número informado, seguido do seu antecessor e 
# do seu sucessor

n = int(input('Digite um numero inteiro: '))
antecessor = n-1
sucessor = n+1

print('O número digitado foi ', n,',o seu antecessor é ', antecessor, 'e o sucessor é ', sucessor)

#solução do professor
# numero = int(input('Informe um número inteiro qualquer: '))
# print(f'O antecessor do número {numero} é {numero - 1}, e o sucessor é {numero + 1}')