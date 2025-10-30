#Utilizando Módulos

#para utilizar um módulo, você deve importar ele com a palavra reservada import
#isso vai disponibilizar todas as funções e recursos do módulo
#exemplo: import math
#é possível importar também apenas partes do módulo, utilizando from ... import ...
#exemplo: from math import sqrt, floor

#desafio 16
# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.
import math
from math import floor, sqrt, hypot, radians, sin, cos, tan
import random

# num = float(input('Digite um numero real qualquer: '))
# print(f'O número digitado foi {num} e a sua porção inteira é {floor(num)}')


#desafio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# Fórmula: hipotenusa = √(cateto_oposto² + cateto_adjacente²)
# catop = float(input('Digite o comprimento do catesto oposto: '))
# catadj= float(input('Digite o comprimento do cateto adjacente: '))
# print(f'O comprimento da hipotenusa é {hypot(catop,catadj):.2f}')

#desafio 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
# angulo = float(input(' Digite um angulo Em GRAUS para ver o seno cosseno e tangente: '))
# anguloradiano = radians(angulo)
# print(f' o Seno do angulo de {angulo}º é {sin(anguloradiano):.2f}, o cosseno é {cos(anguloradiano):.2f} e a tangente é {tan(anguloradiano):.2f}')

#desafio 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# aluno1=str(input('Digite o nome do primeiro aluno: '))
# aluno2=str(input('digite o nome do segundo aluno: '))
# aluno3=str(input('Digite o nome do terceiro aluno: '))
# aluno4=str(input('digite o nome do quarto aluno: '))
# lista =[aluno1, aluno2, aluno3, aluno4]
# escolhido = random.choice(lista)
# print(f'O Aluno escolhido foi {escolhido}')


#desafio 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# aluno1=str(input('Digite o nome do primeiro aluno: '))
# aluno2=str(input('digite o nome do segundo aluno: '))
# aluno3=str(input('Digite o nome do terceiro aluno: '))
# aluno4=str(input('digite o nome do quarto aluno: '))
# lista =[aluno1, aluno2, aluno3, aluno4]
# random.shuffle(lista)
# print(f'A ordem de apresentação será {lista}')



#desafio 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# import pygame
# pygame.init()
# pygame.mixer.music.load('file_example_MP3_700KB.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()