# ler od dados
# dae um display de um dashboard para o time
# exibir dados de um jpogador especifico
time = list()
list_gols = list()
while True:
    stats = dict()
    stats['nome'] = str(input('Nome do jogador: '))
    stats['jogos'] = int(input('quantos jogos o cara jogou?: '))
    
    for g in range(0,stats['jogos']):
        list_gols.append((int(input(f'Quantos gols {stats["nome"]} fez na {g} partida?: '))))
    stats['gols'] = list_gols[:]
    stats['total_gols'] = sum(list_gols)
    list_gols.clear()
    time.append(stats.copy())
    ask = input('quer continuar? [S/N]').lower()
    if ask in 'Nn':
        break
total = sum(list_gols)
print(time)

for i in stats.keys():
    print(f'{i:<15}',end = '')
print()
for k,v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-'*40)

while True:
    busca = int(input('Quer busccar dados de qual jogador? (999 para)'))
    if busca == 999:
        break
    print(f'Levantamento de dados do jogador {time[busca]["nome"]}:')
    for e,m in enumerate(time[busca]['gols']):
        print(f'no jogo {e} {time[busca]["nome"]} fez {g} gols')
        print()