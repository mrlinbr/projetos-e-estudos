from random import randint
jogadores = []
jogador = {}
for j in range (0,4):
    jogador['nome'] = input('nome: ')
    jogador['numero'] = randint(1,7)
    jogadores.append(jogador.copy())
print(jogadores)
maior = 0
maior_jog = ''
for i in range(0,len(jogadores)):
    print(jogadores[i]['numero'])
    n = jogadores[i]['numero']
    if i == 0:
        maior = n
    else:
        if n > maior:
            maior = n
            maior_jog = jogadores[i]['nome']
print(f'o jogador {maior_jog} foi o vencedor, com {maior} pintos')