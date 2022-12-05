#programa para advinhar um numero entre 0 e 5
"""
import random
n = random.randint(0,5)
x = int(input('guess teh number betwen 0 and 5: '))
if x == n:
    print('you guessed right!!!')
else:
    print('not this time, try again')"""
#programa para calcular a multa com base na velocidade
"""
vel = float(input('velocidade: '))
if vel >80:
    print ('passou dos limites meu chapa! sua multa vai ser de {}R$'.format((vel-80)*7))
else:
    print('ok, tudo nos conformes!')
"""
#programa para ver se um numero é par ou impar
"""
num = int(input('digite o numero: '))
nao sei kkk
"""

#custo da viagem
"""
pas= float(input('qual a distancia a ser percorrida?'))
if pas<200:
    print('sua viagem custará{}'.format(pas*0.50))
else:
    print('sua é longa, então custará {}'.format(pas*0.45))
"""
#calcular ano bissexto
"""
num = int(input('digite o ano em questão: '))
n= num % 4
if n == 0:
    print('{} é um ano bissexto'.format(num))
else:
    print('{} não é um ano bissexto'.format(num))
"""
#Leia tres numero s ediga qual é o maior
'''
a = int(input('digite um numero:'))
b = int(input('digite um numero:'))
c = int(input('digite um numero:'))
lst = [a,b,c]
print('o maior numero é {}'.format(max(lst)))
print('o menor numero é {}'.format(min(lst)))
'''
#um programa par acalcular um aumento de 10% se o funcionario ganhar mais de 1.250
#e 15% caso ganhe mais
'''
sal = float(input('Qual o seu salário? '))
if sal>1250:
    print('seu novo salário será de {}'.format(((sal/100)*10)+sal))
else:
    print('seu novo salário será de {}'.format((sal/100)*15+sal))
'''