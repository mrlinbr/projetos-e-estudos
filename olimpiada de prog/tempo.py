#um programa para alocar os participantes de um torneio em seus determinados grupos.
"""
o programa deve:
    Ler a lista com o resultados do participante.
    calcular a quantidade de vitorias que o participante obteve, percorrendo a lista e armazenando as vitorias e derrotas em listas distintas.
    de acordo com a quantidade de vitorias, o participante deve ser alocado no grupo:
        Grupo 1 no caso de 5 ou 6 vitorias.
        Grupo 2 no caso de 3 ou 4 vitorias.
        Grupo 3 no caso de 1 ou 2 vitorias.
        Cas nao haja vitorias, o participante não será classificado.
    """
resultados = []
for e in range (0,6):
    result = input(f"Diga qual foi o resultado do jogo N{e} com [V ou P]: ").lower()
    while result not in 'vp':
        result = input(f"Por favor, use apenas V ou P: ").lower()
    resultados.append(result)

vict = [i for i in resultados if i == 'v']
vitorias = len(vict)
grupo = int()
if (vitorias >=5):
    grupo = 1

elif (vitorias>=3 and vitorias<5):
    grupo = 2

elif (vitorias>0 and vitorias<=2):
    grupo = 3

else:
    grupo = -1

print(grupo)