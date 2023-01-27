"""
printar numeros de forma reversa
"""
#printar os numeros de 1 até 10 de 1 em 1
#printar de  10 até 1 de 1 em 1
#printar de x até y pulando de z em z (pode ser negativo)
from time import sleep
def contador(inicio, fim, passo):
    if passo<0:
        passo*=-1
    if passo == 0:
        passo = 1
    if inicio>= fim:
        while inicio >= fim:
            print(inicio, end = ' ', flush=True)
            inicio -= passo
            sleep(0.5)
    else:
        while inicio<= fim:
            print(inicio, end =' ', flush=True)
            inicio+=passo
            sleep(0.5)

contador(1,10,2)
print()
contador(10,1,2)
ini = int(input('\ndigite o inicio '))
fi = int(input('digite o fim '))
pas = int(input(f'digite o passo '))
contador(ini,fi,pas)