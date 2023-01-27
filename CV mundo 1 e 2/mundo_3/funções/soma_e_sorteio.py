from random import randint
from time import sleep

lista = list()
def sortear():
    for i in range(0,6):
        lista.append(randint(1,100))
    for e in lista:
        print(e, end = ' ')

def somar():
    soma = 0
    cont = list()
    for n in lista:
        if n%2 == 0:
            soma += n
            cont.append(n)
    print(f'\nA soma dos numeros pares em lista é de {soma},sendo {len(cont)} ({cont})')
sortear()
somar()