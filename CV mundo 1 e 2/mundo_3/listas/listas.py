'''
l = []
for i in range (0,5):
    n = int(input('digite um numero: '))
    l.append(n)
print(f'o maior valor digitado foi {max(l)} e o menor foi {min(l)}')
'''
#varios valores entram, se for repetido não é adicionado e no final é mostrado em ordem crescente
''''
l = []
while True:
    n = int(input('Digite um valor para a lista: '))
    if n in l:
        l.pop()
        print('o valor já está presente na lista, não vou adicionar...')
    l.append(n)
    ask = str(input('quer continuar? [S/N]'))
    if ask not in 'SsNn':
        ask = str(input('quer continuar? [S/N]'))
    if ask in 'Nn':
        break
    l.sort()
print(f'os valores adicionados nesta lista foram {l}')
'''
#adicioanr valors na lsta seguindo uma ordem]
'''
list_num = []
des_lst = []
print('vamos dispor os numeros que voce digitar em uma segquenciaa crescente, independente da ordem.\n')
for i in range (0,5):
    n = int(input('Ditite um numero: '))
    des_lst.append(n)
    if i == 0 or n > list_num[-1]:
        list_num.append(n)
    else:
        while True:
            pos = 0
            if n <= list_num[pos]:
                list_num.insert(pos,n)
                break
            pos +=1
print(f'a lista em ordem é {list_num}, enquanto ela desordenada é {des_lst}')
'''
#ler uma lista de n numeros e dizer o coprimento dela, ela ao contrario e se o nuemro 5 apareceu
'''
lista = []
print('digite qualquer palavra para finalizar o programa')
while True:
    try:
        inpt = int(str(input('Digite um numero para adicionar a lista: ')))
        lista.append(inpt)
    except:
        break
    
print(lista)
print(f'o numero de elemntos nessa lista foi {len(lista)}')
lista.sort(reverse=True)
print(f'a lista ao contrario é {lista}')
if 5 in lista:
    print('o numero 5 foi digitado ', end='')
    print(f'{lista.count(5)} vezes')
else:
    print('o numero 5 não foi digitado')
'''
#um programa que lê ua lista e em seguida vai adiconando os numeros pares e impares em listas diferentes
'''
lst = []
pares = []
impares = []
while True:
    try:
        n = int(input('digite um numero: '))
        lst.append(n)
    except:
        break
for i in range(0, len(lst)):
    if lst[i]  % 2 == 0:
        pares.append(lst[i])
    else:
        impares.append(lst[i])
print(f'a lista completa foi {lst}\na lista de nuemros pares{pares}\ne a de impares {impares}')
'''
#validando expressões
exp = str(input('digite a expressão: '))
direita = direita = soma = 0
direita = exp.count('(')
esquerda = exp.count(')')
soma = direita + esquerda
if soma % 2 == 0:
    print('a expressão está correta')
else:
    print('errou, conserta aí')