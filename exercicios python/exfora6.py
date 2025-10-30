#Desenvolva um programa que armazene quatro notas em uma 
# lista e que apresente a média final. 
# Caso a média seja igual ou superior a 7, 
# apresentar a mensagem "APROVADO", caso contrário, 
# armazenar a nota da prova final e recalcular a média. 
# Caso a nova média seja igual superior a 5, 
# apresentar a mensagem "APROVADO", caso contrário, 
# apresentar a mensagem "REPROVADO"

#Desenvolva um programa que armazene quatro notas em uma 
# lista e que apresente a média final.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
notas =[n1, n2, n3, n4]
print( 'A media final é:' , (n1+n2+n3+n4)/4)

media = (n1+n2+n3+n4)/4

# Caso a média seja igual ou superior a 7, 
# apresentar a mensagem "APROVADO", caso contrário, 
# armazenar a nota da prova final e recalcular a média

if media >= 7:
    print('APROVADO')
else:
    n5 = float(input('Digite a nota da prova final: '))
    medianova = (media + n5) /2
    print('A nova média é:', medianova)
# Caso a nova média seja igual superior a 5, 
# apresentar a mensagem "APROVADO", caso contrário, 
# apresentar a mensagem "REPROVADO"
    if medianova >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')

#solução do professor
# notas = []
# contador = 1

# while contador < 5:
#     notas.append(int(input(f'Informe a {contador}ª nota: ')))
#     contador += 1

# media = sum(notas) / len(notas)
# print(f'Sua média final foi {media}')
# if media >= 7:
#     print('APROVADO')
# else:
#     notas.append(int(input('Informe a nota da prova final: ')))

#     media = sum(notas) / len(notas)
#     print(f'Sua média final foi {media}')
#     if media >= 5:
#         print('APROVADO')
#     else:
#         print('REPROVADO')       
