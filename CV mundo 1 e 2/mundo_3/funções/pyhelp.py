#um sistema de ajuda, onde o usuario digite o nome da função ou biblioteca
def helpi(tag):
    print(help(tag))

while True:
    cmd = str(input("'parar' fecha\n Função ou Biblioteca: "))
    if cmd == 'parar':
        break
    helpi(cmd)
"preguiça de usar cores"