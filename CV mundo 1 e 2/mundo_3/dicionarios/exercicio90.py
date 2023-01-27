#media dos jogadores
jogadores = dict()
jogadores['nome']= str(input('nome: '))
jogadores['media']= float(input('media: '))
print(f'o jogador {jogadores["nome"]} foi:', end= '')
print(f'aprovado') if jogadores["media"]>6 else print('reprovado')