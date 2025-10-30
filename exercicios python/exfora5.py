#Desenvolva um programa que armazene quatro notas 
# em uma lista e que apresente: 
# a média final, a maior nota e a menor nota

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

notas =[n1, n2, n3, n4]

print( 'A media final é:' , (n1+n2+n3+n4)/4, 'A maior nota é: ', max(notas),'A menor nota é: ', min(notas))

#solução do professor
# notas = []
#contador = 1

#while contador <= 4:
#    notas.append(float(input(f'Digite a {contador}ª nota: ')))
#    contador += 1  
#maiornota = max(notas)
#menornota = min(notas)
#medianotas = sum(notas) / len(notas)
#print(f'A media final é {medianotas:.2f}, a maior nota é {maiornota} e a menor nota é {menornota}')