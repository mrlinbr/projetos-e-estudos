#refazendo a função que lê numeros inteiros.
def ler_inteiro(texto):
    while True:
        try:
            num = int(input(f'{texto}'))
        except (ValueError,TypeError):
            print('Tipo de argumento invalido. tente novamente')
        except(KeyboardInterrupt):
            print('o cara parou de digitar.')
        else:
            return num

def ler_real(texto):
    while True:
        try:
            num = input(f'{texto}')
            num = num.replace(',','.')
            n_num = float(num)
        except (ValueError,TypeError):
            return n_num
        except(KeyboardInterrupt):
            print('o cara parou de digitar.')
        else:
            return num
inteiro = ler_inteiro('digite um numero: ')
real = ler_real('agora um numero quebrado: ')
print(f'voce digitou {inteiro}', end = ' ')
print(f'e depois {real}')
