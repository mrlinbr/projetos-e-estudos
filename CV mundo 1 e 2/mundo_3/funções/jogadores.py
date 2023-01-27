#uma função para ler a ficha de um jogador, recebendo o nome e quantidade de gols
def cadastro(nome = '<desconhecido>', gols = 0):
    print(f'o jogador {nome} fez {gols} gols')


n = input('digite o nome: ')
g = input('quantidade de gols: ')

if n.strip() == '':
    cadastro(gols = g)
else:
    cadastro(n,g)

if g.isnumeric():
    g = int(g)
else:
    g = 0
cadastro(n,g)