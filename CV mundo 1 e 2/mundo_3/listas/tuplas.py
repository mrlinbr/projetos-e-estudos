'''
from num2words import num2words
op = ''
while True:
    if op == 'N':
        break 
    num= int(input('digite um numero\n'))
    n_extenso = num2words(num,lang = 'pt-br')
    print(f'voce digitou o numero {n_extenso}')
    op = str(input('quer continuar? [S/N]')).strip().upper()[0]
print('programa finalizado')
'''
#tabela com os colocados no brasileirão 2022
'''
classificação = ('palemiras', 'internacional', 'corintans', 'flamengo', 'bahia', 'chapecoense', 'avai', 'bragantino')
print('_-'*10)
print(classificação[:5])
print('-_'*10)
print(classificação[4:])
print('_-'*10)
print(sorted(classificação))
print('_-'*10)
pos = classificação.index('chapecoense')
print(f'chapecoense se encontra na {pos+1} posicção')
'''
#crie uma tupla com 5 numeros aleatorios e em seguida exiba qual foi o menor valor e qual foi o maior valor.
'''
como eu adiciono itens a uma tupla de froma automatica?
como eu posso exibir o menor e maior valor desta tupla?
'''
'''
from random import randint
from time import sleep
while True:
    n = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),)
    for num in n:
        print(f'{num}, ', end = '')
    print('')
    print(max(n))
    print(min(n))
    sleep(2)
    if max(n) == 5:
        break
print('prigrama finalizado')
'''
#um daqueles programas que lêem numeros e fazem coisas
'''
n = (
    int(input('um valor: ')),
    int(input('um valor: ')),
    int(input('um valor: ')),
    int(input('um valor: '))
    )
print(n)
par = impar = 0
for num in range(0,len(n)):
    if n[num]%2 == 0: par +=1
    else: impar += 1
var9 = n.count(9)
print(f'o numero 9 aparece {var9} vezes na tupla') if var9>=1 else print('não existe numero nove')
print(f'o numero 3 aparece na posição {n.index(3) + 1}') if 3 in n else print('o numero 3 não está na tupla')
print(f'foram digitados {par} numeros pares e {impar} numeros impares, sendo os pares ', end = '')
for i in range (0, len(n)):
    if n[i]%2==0:
        print(n[i], end = ' ')
'''
#achar vogais
'''
palavra = ('murilo','pedro','gustavo','viviane','iracema')
for p in palavra:
    print(f'\nA palavra {p.upper()} tem como vogais as letras ', end ='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end ='')
'''
#honestamente, odiei as tuplas... muitos limitadas e cheias de putaria
def no_space(x):
    str_char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            str_char += '_'
        else:
            str_char = str_char + x[i]
    return str_char

nome = input('digite alguma coisa: ')
print(no_space(nome))

