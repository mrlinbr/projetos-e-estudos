def maior_num(*numeros):
    print(f'Voce digitou esses numeros: ', end='')
    lst  = []
    for i in numeros:
        for n in numeros[numeros.index(i)]:
            lst.append(n)
    
    maior = 0
    for i in lst:
        if lst[0] == i:
            maior = lst[0]
        else:
            if i>maior:
                maior = i
    
    print(f'o maoir valor pela funçãodificil foi {maior}')
    print(f'já pela função do pyhton, foi {max(lst)}')


from random import randint
lista = []
for i in range(0,11):
    lista.append(randint(1,100))
print(lista)
maior_num(lista)