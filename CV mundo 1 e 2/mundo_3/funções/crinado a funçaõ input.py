#uma função que so recebe numero
def validar(t = '', i = ''):
    print(t,end = '')
    i = input('')
    if i.isnumeric():
        return i 
    else:
        print('nao é numerico kkk')

n = validar('Digite um numero: ')
print(f'voce digitou o numero {n}')