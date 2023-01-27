#Uma função para printar na tela linhas que acompanhem um texto

def printador(pal):
    cont = 0
    for i in pal:
        cont += 1
    print('~'*cont)
    print(pal)
    print('~'*cont)


palavra = input('digite uma palavra: ')
printador(palavra)