#Um programa ara ler varios numeros ate que oinput seja 999, e então exiba a quantidade de numeros digitados
'''
total = soma = 0
while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    total +=1
    soma += num
print(f'voce digitou {total} numeros e a soma deles foi {soma}')
'''
#tabuada maneira
'''
quant = int(input('quantos numeros voce deseja que sejam exibidos? '))
while True:
    num = int ( input('digite um numero: '))
    if num<=0:
        print('programa finalizado com sucesso')
        break
    print('_-'*20)
    for i in range (1,quant+1):
        
        print(f'{num} x {i} = {num*i}')
    print('_-'*20)
'''
#par ou impar'
'''
print('vamos jogar par ou impar ')
from random import randint
count = 0
while True:
    comput = randint(0,10)
    user = int(input('digite o seu numero '))
    choice = str(input('par ou impar? [P/I] ')).upper().strip()[0]
    num = comput+user

    if choice == 'P':
        if num%2 ==0:
            print('usuario ganhou!')
            count += 1
        else:
            print(f'eu ganhei, otario. escolhi {num} então deu {num+user}')
            break

    if choice == 'I':
        if num%2 != 0 :
            print('usuario ganhou')
            count += 1
        else:
            print(f'eu ganhei, otario. escolhi {num} entã deu {num+user}')
            break
print(f'voce ganhou {count} vezes')
'''
#cadastramento de clientes
'''
maiores_de_18 = homens = mulheres_adultas = 0 
while True:
    idade = int( input('Qual a idade? '))
    sexo = str(input('qual o sexo? [Mm/Ff]'))

    if idade > 18:
        maiores_de_18 += 1
    
    if sexo in 'Mm':
        homens += 1

    if sexo in 'Ff':
        if idade > 20:
            mulheres_adultas += 1
        else:
            pass

    pergunta = str(input('Quer ocntinuar? [S/N]')).upper()
    print('\n\n')

    if pergunta == 'N':
        break
print(f'o total de pessoas maiores de 18 foi {maiores_de_18}, já de hoemns foi {homens} enquanto tivemos {mulheres_adultas} mulheres maiores de 20')
'''
#