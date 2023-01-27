# um programa para calcular a area e um dado terreno,ultilizando funções
def calc():
    x = float(input(f'Digite a largura de seu terreno: '))
    y = float(input(f'Digite a altura de seu terreno: '))
    print(f'As dimensões do seu terreno de {x}m por {y}m é de {x*y}m^2')

for i in range (0,3):
    calc()