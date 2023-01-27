#um programa que vai ler o nome, numero de partidas e gols de um jogador, e no final, mostrar tudo isso na tela
jogador = {}
nome = input('Qual o nome do jogador? ')
gols_lista = []
jogador['nome_jogaodr'] = nome
n_partidas = int(input(f'Quantas partidas {nome} jogou? '))

for i in range (0,n_partidas):
    gols_partida = int(input(f'     Quantos gols {nome} marcou na partida de numero {i+1}? '))
    gols_lista.append(gols_partida)
jogador['gols'] = gols_lista[:]
jogador['total_gols'] = sum(gols_lista)

print('¨-'*20)
print(jogador)
print('¨-'*20)
for i,o in jogador.items():
    print(f'O campo {i} tem o valor {o}')
print('¨-'*20)
print(f'O jogador {nome} jogou {n_partidas}:')
for j in range(0,len(gols_lista)):
    print(f'    na partida {j+1} {nome} fez {gols_lista[j]} gols')
print(f'No total, {nome} fez {jogador["total_gols"]} gols')