#crie uma fução parecida com o input do python, mas que vai
# 1- Aceitar apenas valores numericos
# 2- Converter a virgula de um numero em um ponto (ex: 55,99) OK

def leiaMoney(enunciado):
    while True:
        valor = str(input(f'{enunciado}: '))
        valor.strip()
        if ',' in valor:
            valor = f'{valor}'.replace(',','.')
        for i in valor:
            if i not in range(0,9):
                if i == '.':
                    pass
                else:
                    print(f'{valor} não é um valor valido, digite novamente')
                    #que função de merda kkk, a outra faz a mesma coisa mas de uma forma mais simples
                    
def lerDinheiro(enunciado):
    while True:
        valor = input(f'{enunciado}: ')
        if ',' in valor:
            valor = f'{valor}'.replace(',','.')
        try:
            valor = float(valor)
            break
        except:
            print(f'ERRO! {valor} nã é um valor valido. Tente novamente.')
    return valor

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
            num = float(input(f'{texto}'))

        except (ValueError,TypeError):
            print('Tipo de argumento invalido. tente novamente')
        except(KeyboardInterrupt):
            print('o cara parou de digitar.')
        else:
            return num