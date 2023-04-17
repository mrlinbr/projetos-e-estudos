#um programa que receba uma lista com varios numeros
#sempre que houver um 'zero', ele vai apagar o numero antecessor a este zero
"""
Ler os numeros e armazena-los numa lista. 10 -14
Percorrer essa lista e indentificar onde há um 0
apagar o 0 e o numero que esta na posição 'zero[-1]' da lista. 16 - 20
Somar os numeros restantes da lista.
"""

len = int(input('Qual o tamanho da lista?: '))
lst = []
soma_lst = []
for i in range(0,len):
    num = int(input('Qual o numer0, chefia?: '))
    lst.append(num)

for n in lst:
    if n == 0:
        print(lst.index(n))
        pos = lst.index(n)
        lst.pop(pos-1)
        lst.pop(pos)

total = 0    
for g in lst:
    total += g

print('\n\n')
print(lst)
print(total)