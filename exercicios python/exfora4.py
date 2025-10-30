#Desenvolva um programa que tenha uma função que verifique se um 
#número inteiro qualquer é par ou impar



def verificanumero(numdigitado):
	if int(numdigitado) % 2 == 0:
		print('o número é par')
	else: 
		print('o numero é impar')

numdigitado = input('Digite um número inteiro: ')
numeroverificado = verificanumero(numdigitado)
print(numeroverificado)