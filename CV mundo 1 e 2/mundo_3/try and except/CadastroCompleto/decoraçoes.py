def linha_simples():
    print('_'*30)

def linha_pontilhada():
    print('-'*30)

def sequencia_igual(nome,posição = ''):
    print('='*30)
    print(f'{posição} - {nome.upper()}')
    print('='*30)

def menu(*items):
    from time import sleep
    c = 1
    print('MENU DO PROGRAMA'.center(25))
    for i in items:
        sequencia_igual(i,c)
        c +=1
    print(f'Agora escolha uma das opções acima:')
    while True:
        try:
            op = int(input(''))
            items[op-1]
        except (ValueError, TypeError):
            print('ERRO!!! DIGITE UM NUMERO')
        except (IndexError):
            print('ERRO!!! valor nao consta dentre as opções.')
        else:
            print(items[op-1])
            return op
menu('ver lista','cadastrar','sair')