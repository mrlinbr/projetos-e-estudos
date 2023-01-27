#crie um programa que leia o nome e peso de varias pessoas e em seguida dia quais foram as  mais pesadas e mais leves
"""
individuo = list()
pessoas = list()
maior = menor = 0
print('DIgite "parar" em nome para parar o programa')
while True:
    individuo.append(str(input("digite um nome: ")))
    individuo.append(int(input('qual o peso?: ')))
    if len(individuo) == 0:
        maior = menor = individuo[1]
    else:
        if individuo[1]>maior:
            maior = individuo [1]

        if individuo[1]<menor:
            menor = individuo[1]
    
    pessoas.append(individuo[:])
    individuo.clear()
    rspt = input('quer continuar? [S/N]')
    if rspt in 'Nn':
        break

print(individuo)
print(pessoas)
print(maior, menor)
print(f'{"pessoa"} é a pessoa mais pesada porque tem {maior} enquanto {"outra_pessoa"} tem {menor}')
"""
#um programa que recebe numeros e armazena eles dentro de uma lista, separendo-os entre pares e impares
'''
todos = [[],[]]

for i in range (0,7):
    num = int(input('Digite um numero: '))
    if num%2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
print(todos)
todos[0].sort()
todos[1].sort()
print(todos)
print(f'os numero pares foram {todos[0]}')
print(f'e os impares foram {todos[1]}') 
'''
#matriz e numeros
#leio 9 numeros e os adicono numa lista, dai vou dando printo formatado com o indice do fro no meio
#for dentro de for, assim n preciso me repetir
"""
numeros = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma_terceira = 0
maior_segunda = []
for c in range(0,3):
    for l in range(0,3):
        numeros[c][l] = int(input(f'diga um numero para a posição {c}/{l}: '))
for n in range(0,3):
    for i in range(0,3):
        print(f'[{numeros[n][i]:^3}]',end='')
        if numeros[n][i]%2==0:
            soma += numeros[n][i]
    print()
for k in range(0,3):
    soma_terceira += numeros[k][2]    
'posso fazer um jogo da velha com isso'
print(f'a soma dos numeros pares é {soma}')
print(f'a soma dos numeros da terceira coluna é {soma_terceira}')
print(f'o maior valor da segunda linha é {max(numeros[1])}')
""" #jogando na mega sena
'''
from random import randint
from time import sleep
n = int (input('Quantos jogos voce quer? '))
for i in range(0,n):
    lst = []
    while len(lst)<=6:
        num = randint(0,60)
        if num not in lst:
            lst.append(num)
    lst.sort()
    print(f'jogo [{i+1}]: {lst}')
    sleep(1)
print('-+'*5,'BOA SORTE MEU CRIA','+-'*5)
'''
#lista de alunos
'''
alunos = []
individuos = []
while True:
    nome= (str(input('Nome: ')))
    n1= (float(input('nota 1: ')))
    n2= (float(input('nota 2: ')))
    individuos.append([nome,[n1,n2],(n1+n2)/2])
    alunos.append(individuos[:])
    individuos.clear()
    op =str(input('Quer continuar? [S/N] '))
    while op not in 'SsNn':
        op =str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break
print('+='*10,'ALUNOS',10*'=+')
print(f'{"No.":<4}{"aluno":<8}{"media":<10}')
for a in alunos:
    print(f'{a[0]}{a[2]}')
while True:
    ask = int(input('quer ver as notas de qual aluno? (999 para)'))
    if ask == 999:
        break
    print(f's notas de {alunos[ask][0]} foram de {alunos[ask][1]}')
'''