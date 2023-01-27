from random import randint
from time import sleep

dicio = dict()
numeros = []

for n in range(0,4):
    num = randint(0,6)
    while num in numeros:
        num = randint(0,6)
    numeros.append(num)
    dicio[f'jogador {n}'] = num

print('_'*10,'P L A C A R','_'*10)
sorted_dicio = sorted(dicio.items(),key = lambda x:x[1], reverse= True)

placar = ['primeiro', 'segundo', 'terceiro', 'quarto']
for k in range(0,4):
    print(f'o {placar[k]} lugar ficou com o ', end = '')
    print( sorted_dicio[k][0],' com ',sorted_dicio[k][1],'pontos')
    print(numeros)
    