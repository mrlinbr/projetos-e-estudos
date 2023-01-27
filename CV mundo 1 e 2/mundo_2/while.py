'''
sexo = str(input('pls,diga qual o seu sexo: [M/F]'))
while sexo not in 'MmFf':
    sexo = str(input('Por favor, informe um sexo valido: '))
print('Cadastro concluido')
'''

'''
from random import randint
n = randint(0,11)
c = 0
l = 0
while c != n:
    c = int(input(' acabei de pensar em um numero, tente advinhar qual foi\n'))
    if c == n:
        print('numero correto!!!')
        print('foram nescessarias {} tentativas para que você acertasse'.format(l))
    else:
        l +=1
        if c > n:
            print('MENOS. O numero que eu escolhi foi menor que esse.')
        else:
            print('MAIS! escolhi um numero maior.')
'''
'''
programa = False
n1 = int(input('digite o primeiro numero '))
n2 = int(input('digite o segundo numero '))
while programa !=True:
    print('escolhauma das seguintes opções:\n[1] somar \n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    opcao = int(input())
    if opcao == 1:
        print('a soma dos dois valores adiconados é {}\n \n'.format(n1+n2))
    if opcao == 2:
        print('a multiplicação entrs {} e {} é {}'.format(n1,n2,n1*n2))
    if opcao == 3:
        lst = list()
        lst.append(n1)
        lst.append(n2)
        print('entre os dois valores adicionados, o maior é {} \n \n'.format(max(lst)))
    if opcao == 4:
        n1 and n2 == 0
        n1 = int(input('digite o novo numero '))
        n2 = int(input('digite o segundo numero '))
        print('\n \n')
    if opcao == 5:
        from time import sleep
        print('desligando...')
        sleep(3)
        
        programa=True
print('obrigado pela preferencia. volte smepre')
'''

#faça um programa que calcule o fatorial de um determinado numero 
#EX: 3! = 3*2*1 = 6
'''meu pano é fazer um loop que a cada execução reduza em 1 o numero da variavel que receberá o numero
não sei como formatar para formar uma sequencia decrescente...'''
'''
n= int(input('digite o numero que voce quer transformarnum fatorial: '))
string= str()
for c in range (n,0,-1):
    string+='{}*'.format(c)
from math import factorial
print('ao calcularmos {}! que é {} obtemos {}'.format(n,string[:-1],factorial(n)))
'''
#gerador de P.A
'''
for i in range(0,11):
    print(n,'->',end='')
    n+=r
print('operação com for finalizada')
'''
'''
n = int(input('digite o primeiro termo da PA '))
r = int(input('qual será a razão? '))
ctrl = 0
termos = 0
while ctrl+termos<10 + termos:
    print (n,' -> ',end='')
    n+=r
    ctrl+=1
print('\n operação com while finalizada, quantos termos quer a mais?')
novos_termos = int(input())
if novos_termos !=0:
    termos = novos_termos
else:
    print('programa finalizado')
'''
#gerador de P.A masi robusto
'''
n = int(input('digite o primeiro termo da PA '))
r = int(input('qual será a razão? '))
ctrl = 10
termos = False
termos_adicionais=10
while termos == False:
    for i in range(n,n+termos_adicionais):
        print(n,'->',end='')
        n+=r
    novo_termo = int(input('\n quantos termos a mais voce deseja ver? '))
    if novo_termo != 0:
        termos_adicionais == novo_termo
    else:
        termos= True
print('programa finalizado com secesso!')
'''
#sequencia de fibonacci
'''
num1 , num2 = 0,1
cont = 0
lim = int(input('digite ate onde voce quer que a sequencia vá: '))
while cont<=lim:
    cont+=1
    print(num1)
    #adiciona a uma variavel o N1 e o N2 para assim saber o proximo termo
    #dessa forma, 0+1=1, então o N1 agora passa a ser 1 e o  N2 passsa a ser 1 também
    n_termo= num1 + num2

    num1=num2 #substituindo os valores para a proxima execução
    num2=n_termo#n2 agora passa a ser o proximo termo
'''
'''
cont = soma = 0
num= int(input('digite um numero [999 para o programa] '))
while num != 999:
    soma += num
    cont +=1
    num = int(input('digite um numero [999 para o programa] '))
print('a soma dos termos digitados por voce em {} inputs foi {}'.format(cont, soma))
'''
#maior e menor valores
count = soma = 0
tamanho = list()
flag = 0
while flag == False:
    num = float(input('digite um numero: '))
    ask = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    soma += num
    count+=1
    tamanho.append(num)
    if ask == 'N':
        flag +=1
print('voce digitou {} numeros. A media entre eles foi de {}, enquanto o entre o maior ({}) e o menor ({}) foi de {}'.format(len(tamanho),soma/len(tamanho), max(tamanho), min(tamanho),max(tamanho)/min(tamanho)))
