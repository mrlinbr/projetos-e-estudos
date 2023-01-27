#teste com elif e IN
'''
nome = input('qual seu nome? ')
if nome == 'murilo':
    print('que nome lindo!')
elif nome in 'pedro maria joão manu ester tadeu tiago jose':
    print('que nome massa! voce é colega de murilo, não é?')
else:
    print('Que nome legal!')
print('boa noite {}!'.format(nome))
'''
#programa de financiamento de casa
'''
casa = float(input('qual o valor da casa que voce quer comprar?'))
sal = float(input('qual seu salario? '))
anos = int(input('Em quantos anos voce planeja pagar?'))

prestacao = (anos*12)
mensalidade = casa/prestacao
if mensalidade>(sal/100)*30:
    print('Desculpe, mas não podemos financiar sua compra no momento pois {} excede 30% de seu salario:('.format(mensalidade))

else:
    print('Podemos financiar sua compra, obrigado pela preferencia :), as prestações serão de {}'.format(mensalidade))
'''
#esqueci como q faz conversão de bases kkkk
'''
num = int(input('digite um numero para ser convertido:' ))
op= int(input('Para qual base deseja converter? \n[1] binaria \n[2] octal \n[3] hexadecimal\n'))
if op == 1:
    numconv= bin(num)
elif op == 2:
    numconv = oct(num)
elif op == 3:
    numconv = hex(num)
else:
    print('algo deu errado :(')
    pass
print('O numero {} convertido na base de opcão {} se torna {}'.format(num,op,numconv[2:]))
'''
#um programa que lê dois numeros inteiros e diga qual o maior, menor ou se os dois são iguais
'''
n1=int(input('primeiro numero: '))
n2=int(input('segundo numero: '))
lst= [n1,n2]
if n1>n2:
    print('{} é maioir que {}'.format(n1,n2))
elif n2>n1:
    print('{} é maioir que {}'.format(n2,n1))
else:
    print('os dois numeros são iguais!')
'''
#Se alistar pô kkkkkjj
'''
ano = int(input('qual ano você nasceu?? '))
idade = 2022-ano
xanos = 18 - idade
if idade < 18:
    print('eitakkjj falta {} anos para voce se alistar'.format(xanos))
elif idade == 18:
    print('bora ali capin.. digo, se alistar?kkj')
else:
    print('já se passaram', xanos, 'anos, bora ali ficar de boa com a justica?')
'''
#gordo kkkkkjj
'''
import re
from math import pow
massa = float(input('Qual teu peso?\n'))
altura = str(input('Qual tua altura?\n'))
altura = float(re.sub('[^0-9]', '', altura))
alt = altura/100
peso = massa/pow(alt,2)
if peso < 18.5:
     print('Meu fi quer bolacha?')
elif peso >18.5 and peso < 25.0:
     print('Tá shape ein pae?')
elif peso > 25.0 and peso <30.0:
     print('tá gordinho kkkjj')
elif peso > 30.0 and peso < 40:
     print('ai cê já me quebra')
else:
     print('o cara tá mó gordão')
'''
#bagulho de ntação
'''
id = int(input('qual sua idade? \n'))
if id < 9:
    print('mirim')
elif id > 0 and id < 14:
    print('infantil')
elif id > 14 and id < 19:
    print('junior')
elif id > 19 and id < 20:
    print('senior')
else : print ('master')
'''
#analisando angulos de um retangulo
'''
a1 = float(input('diga o primero angulo: '))
a2 = float(input('diga o primero angulo: '))
a3 = float(input('diga o primero angulo: '))
if a1 < a2 + a3 and a2<a1+a3 and a3<a1+a2 :
    print('isso dá um triangulo bacana')
    if a1==a2==a3:print('equilatero')
    elif a1 != a2 != a3!= a1: print('escaleno')
    else: print('isoceles')   
else:print('não dá um triangulo nao véi')
'''
#controle de pagamentos
'''
vlr = int(input('Qual o valor do produto? '))
op = int(input(' [1]à vista dinheiro/cheque\n [2]à vista no cartão\n [3]3em até 2x no cartão\n [4]3x ou mais no cartão\n'))
if op == 1:
    vf = vlr - (vlr/100)*10
elif op == 2:
    vf = vlr - (vlr/100)*5
elif op == 3:
    vf = vlr
elif op == 4:
    vf = vlr + (vlr/100)*20
    par = int(input('quantas parcelas? '))
    print('as parcelas serão de {}'.format(vf/par))    
print('o valor final de seu pagamento será de {}'.format(vf))
'''
#preda papel e tesoura
#nao consegui kkkjj
print(' as opções são:')
print('[0] pedra \n [1]papel \n[2]tesoura')
jog1 = int(input('qual será sua jogada?: '))
