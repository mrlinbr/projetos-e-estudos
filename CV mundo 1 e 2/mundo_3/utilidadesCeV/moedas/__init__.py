def moeda(valor = 0, cifrao = 'R$'):
    return f'{cifrao} {valor}'.replace('.',',')

def dobro(n, f = True):
    """
    Calcula o dobro de um numero
    """
    if f:
        return moeda (n*2)
    else:
        return n*2

def metade(n, f = True):
    """calcula a metade do numero que a função recebe como argumento."""
    if f:
        return moeda(n/2)
    else:
        return n/2

def aumentar(n, porcentagem, f = True):
    
    nmr = n+(n*porcentagem/100)
    if f:
        return moeda(nmr)
    else:
        return nmr

def diminuir(n,porcentagem, f = True):
    nmrmenos = n - (n*porcentagem/100)
    if f:
        return moeda(nmrmenos)
    else:
        return nmrmenos

def traco():
    print('_-'*20)

def resumo (preco, aumento = 15, reducao = 15):
    traco()
    print('RESUMO DOS PREÇOS'.center(30))
    traco()
    print(f'O dobro de {moeda(preco)} é: \t{dobro(preco)}')
    print(f'A metade de {moeda(preco)} é: \t\t{metade(preco)}')
    print(f'{moeda(preco)} menos... {reducao}% vai ser igual a: \t{diminuir(preco,reducao)}')
    print(f'{moeda(preco)} mais... {aumento}% vai ser igual a: \t{aumentar(preco,aumento)}')