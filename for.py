# fogos com uma contagem de 1 segundo 
"""
from time import sleep
for c in range (10,0, -1):
    print (c)
    sleep(1)
print('feliz ano novo!!!')
"""
#Todos os numeros pares entre 1 e 50
'''
for c in range(2,51,2):
    print(c)
'''
#Faça um programa que calcule a soma entre 
#todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
n= 0
x= 0 
num= int(input('digite um numero:'))
for c in range (0,num,3):
    x+=1
    if c %2 == 0:
        pass
    else:
        n+=c
print('a soma dos {} valores é {}'.format(x,n))
"""
#printe os multiplos de um dterminado numero
'''
n=  int (input('digite um numero para ver sua tabuada: '))
y = 1
for x in range(0,9):
    
    print('{} x {} é igual a {}'.format(n,x,n*x))
'''
#seis numeros inteiros, some os que forem impares
'''
y = 0
for c in range (0,6):
    x = int(input('digite um numero: '))
    if x%2== 0:
        pass
    else:
        y +=x
print('a soma dos 6 numeros é{}'.format(y))
'''
#10 termos de uma P.A
'''
print('=-='*20)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('=-='*20)
t=int(input('digite o primeiro termo: '))
r=int(input('qual será a razão? '))
for n  in range(t,t+10):
    print(t)
    t+=r
'''
'Guanabare fez tipo assim kk'
'''
termo = int(input('Qual o primeiro termo? '))
razao = int(input('qual a razao? '))
for c in range(termo,razao+10,razao):
    print('{}'.format(c),end=' > ')
'''
#numero primo
'''
n = int(input('digite um numero vamso ver se le é primo; '))
div = 0
for i in range (1,n+1):
    if n%i==0:
        div+=1
if div>=3:
    print('{} nâo é um numero primo'.format(n))
else:
    print('{} é um numero primo!!!'.format(n))
'''
#aocontrario
'''
frase= str(input('digite uma frase: ')).strip().lower()
palavras = frase.split()
print(palavras)
junto = ''.join(palavras)
inverso= junto[::-1]
if inverso==junto:
    print('é um polondomo')
else:
    print('nao é nao')
'''
#grupos
'''
maior=list()
menor=list()
an=list()
for c in range (0,6):
    ano = int( input('em qual ano voce nasceu? '))
    an.append(ano)
    idade = 2022-ano
    if idade>=18:
        maior.append(ano)
    else:
        menor.append(ano)
print('houveram {} menores e {} maiores de idade, sendo o mais velho aquele que nasceu em {}'.format(len(menor),len(maior),min(an)))
'''
#pesos
peso = list()
for c in range(0,5):
    ps=int(input('qual teu peso? '))
    peso.append(ps)
print('o menor peso registrado foi {} enquanto o maior foi {}'.format(min(peso),max(peso)))